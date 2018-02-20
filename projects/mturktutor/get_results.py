import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAI372FLCQRR6BTEMA",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)


# Retrieve HIT given hit ID

# Use the hit_id previously created
hit_id1 = '35F6NGNVM8JMJ0W5CJLI9M8CDF8T7Z'
hit_id2 = '3HJ1EVZS2OJR22IQ6IDXWQVEKSPR3F'

# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed
result1 = mturk.list_assignments_for_hit(HITId=hit_id1, AssignmentStatuses=['Submitted'])
result2 = mturk.list_assignments_for_hit(HITId=hit_id2, AssignmentStatuses=['Submitted'])

#print result1
#print result2

# Parsing HIT answer
# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict

if result2['NumResults'] > 0:
   for assignment in result1['Assignments']:
      xml_doc = xmltodict.parse(assignment['Answer'])
      
      print "Worker's answer was:"
      if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
         # Multiple fields in HIT layout
         for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
            print "For input field: " + answer_field['QuestionIdentifier']
            print "Submitted answer: " + answer_field['FreeText']
      else:
         # One field found in HIT layout
         print "For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier']
         print "Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText']
else:
   print "No results ready yet"


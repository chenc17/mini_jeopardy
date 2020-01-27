import mini_jeopardy
import requests #module for making API requests
from datetime import datetime #module for creating the date parameters for the API requests
import random
import sys

#clues for collection_1_test_3
test_cleaned_clues = [{'id': 13595, 'answer': 'Salt', 'question': "It's the more common name for sodium chloride", 'value': 100, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:14.962Z', 'updated_at': '2014-02-11T22:54:14.962Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 13601, 'answer': 'Biennial', 'question': 'Foxglove is an example of this type of plant that completes its life cycle in 2 years', 'value': 200, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.054Z', 'updated_at': '2014-02-11T22:54:15.054Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 13607, 'answer': 'Venus', 'question': 'After the sun & moon, this planet is the brightest object in the sky', 'value': 300, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.181Z', 'updated_at': '2014-02-11T22:54:15.181Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 13613, 'answer': 'Hydrogen', 'question': 'The pH in pH scale stands for the "potential of " this element', 'value': 400, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.276Z', 'updated_at': '2014-02-11T22:54:15.276Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 13619, 'answer': 'Trapezoid', 'question': "In geometry it's a quadrilateral with 2 parallel sides; in anatomy, it's the smallest wrist bone", 'value': 500, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.374Z', 'updated_at': '2014-02-11T22:54:15.374Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14138, 'answer': 'Glaciers', 'question': 'Drumlins are elongated, elliptical hills formed at the edges of these moving ice masses', 'value': 100, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.063Z', 'updated_at': '2014-02-11T22:54:31.063Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14144, 'answer': 'Periodic Table of Elements', 'question': 'Elements are arranged in order of their atomic numbers on this table', 'value': 200, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.145Z', 'updated_at': '2014-02-11T22:54:31.145Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14150, 'answer': 'Sulphur', 'question': 'This yellow element is found in gunpowder & matches & is used in vulcanizing rubber', 'value': 300, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.255Z', 'updated_at': '2014-02-11T22:54:31.255Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14156, 'answer': 'Yogurt', 'question': '2 bacteria, Lactobacillus Bulgaricus & Streptococcus Thermophilus, turn milk into this', 'value': 400, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.337Z', 'updated_at': '2014-02-11T22:54:31.337Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14162, 'answer': "Foucault\\'s Pendulum", 'question': "Named after its 19th century inventor, this pendulum demonstrates the Earth's rotation", 'value': 500, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.419Z', 'updated_at': '2014-02-11T22:54:31.419Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14228, 'answer': 'caffeine', 'question': 'Among alkaloids found in plants, this stimulant is found in coffee or tea', 'value': 100, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.615Z', 'updated_at': '2014-02-11T22:54:33.615Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14234, 'answer': 'intelligence quotient', 'question': 'You may not need a high IQ to know IQ stands for this', 'value': 200, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.698Z', 'updated_at': '2014-02-11T22:54:33.698Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14240, 'answer': 'metamorphosis', 'question': 'Name for the process a caterpillar goes through to become a moth', 'value': 300, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.781Z', 'updated_at': '2014-02-11T22:54:33.781Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14246, 'answer': 'streptococci', 'question': "When cocci live in pairs, they're called diplococci; in clusters, staphylococci; in chains, this", 'value': 400, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.895Z', 'updated_at': '2014-02-11T22:54:33.895Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 20348, 'answer': 'hair', 'question': 'Hirsutism is having more than the normal amount of this', 'value': 100, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:55.719Z', 'updated_at': '2014-02-11T22:57:55.719Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 20354, 'answer': 'delta', 'question': 'This 4th letter of the Greek alphabet is used to describ a high-speed aircraft wing type', 'value': 200, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:55.819Z', 'updated_at': '2014-02-11T22:57:55.819Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 20360, 'answer': 'the lens', 'question': 'The focal length is the distance from the center of one of these to the focal point', 'value': 300, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:55.940Z', 'updated_at': '2014-02-11T22:57:55.940Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 20366, 'answer': "Halley\\'s comet", 'question': 'When astronomers got a close-up look at this object in 1985-86, its nucleus looked like a big potato', 'value': 400, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:56.043Z', 'updated_at': '2014-02-11T22:57:56.043Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 20372, 'answer': 'interglacial', 'question': "This term refers to the warm periods within ice ages; we're in one of those periods now", 'value': 500, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:56.139Z', 'updated_at': '2014-02-11T22:57:56.139Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}]

#clues for collection 2 tests
test_sorted_clues = [{'id': 14138, 'answer': 'Glaciers', 'question': 'Drumlins are elongated, elliptical hills formed at the edges of these moving ice masses', 'value': 100, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.063Z', 'updated_at': '2014-02-11T22:54:31.063Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14144, 'answer': 'Periodic Table of Elements', 'question': 'Elements are arranged in order of their atomic numbers on this table', 'value': 200, 'airdate': '1996-01-24T12:00:00.000Z', 'created_at': '2014-02-11T22:54:31.145Z', 'updated_at': '2014-02-11T22:54:31.145Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 14240, 'answer': 'metamorphosis', 'question': 'Name for the process a caterpillar goes through to become a moth', 'value': 300, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.781Z', 'updated_at': '2014-02-11T22:54:33.781Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 13613, 'answer': 'Hydrogen', 'question': 'The pH in pH scale stands for the "potential of " this element', 'value': 400, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.276Z', 'updated_at': '2014-02-11T22:54:15.276Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}, {'id': 20372, 'answer': 'interglacial', 'question': "This term refers to the warm periods within ice ages; we're in one of those periods now", 'value': 500, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:56.139Z', 'updated_at': '2014-02-11T22:57:56.139Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}]

#TESTING CLUE COLLECTION

#Test 1: Check that calling get_clues() with the correct parameters
#results in 19 clues where the clues all aired in 1964
def collection_1_test_1():

    print_opener('collection_1_test_1','Check that calling get_clues() with the correct parameters results in 19 clues that aired in 1964')
    #valid dates
    min_date = datetime.strptime('01/01/1996,00:00:00,UTC', '%m/%d/%Y,%H:%M:%S,%Z')
    max_date = datetime.strptime('12/31/1996,23:59:59,UTC', '%m/%d/%Y,%H:%M:%S,%Z')

    parameters = {
     'category':25,
     'min_date':min_date,
     'max_date':max_date
    }

    clues = mini_jeopardy.get_clues(parameters)

    num_clues = 0
    invalid_air_date_seen = False
    for clue in clues:
        num_clues = num_clues + 1
        #dates look like this "1985-02-08T12:00:00.000Z"
        if (clue['airdate'][0:4]!='1996'):
            invalid_air_date_seen = True

    expected_output_num_clues = 19
    expected_output_invalid_air_date_seen = False
    print('Expected number of clues: ',expected_output_num_clues)
    print('Actual number of clues: ',num_clues)
    print('Any air dates outside 1996?: ',invalid_air_date_seen)

    status = 'fail'
    if (num_clues==expected_output_num_clues and invalid_air_date_seen==expected_output_invalid_air_date_seen):
        status = 'pass'

    print('Status: '+status)


#Test 2: Check that calling get_clues() with invalid parameters
#results in an empty list
def collection_1_test_2():

    print_opener('collection_1_test_2', 'Check that calling get_clues() with invalid parameters results in an empty list')
    #invalid dates
    min_date = datetime.strptime('01/01/1900,00:00:00,UTC', '%m/%d/%Y,%H:%M:%S,%Z')
    max_date = datetime.strptime('12/31/1900,23:59:59,UTC', '%m/%d/%Y,%H:%M:%S,%Z')

    parameters = {
     'category':25,
     'min_date':min_date,
     'max_date':max_date
    }

    actual_output = mini_jeopardy.get_clues(parameters)

    expected_output = []
    print('Expected output: ',expected_output)
    print('Actual output: ',actual_output)

    status = 'fail'
    if (expected_output==actual_output):
        status = 'pass'

    print('Status: '+status)

#Test 3: Check that calling pick_and_sort() results in clues with different
#values that are sorted in ascending order
def collection_1_test_3():

    print_opener('collection_1_test_3', 'Check that calling pick_and_sort() results in clues with different values that are sorted in ascending order')

    clues = mini_jeopardy.pick_and_sort(test_cleaned_clues)

    #data to test the logic of the test
    # clues = [{'id': 20372, 'answer': 'interglacial', 'question': "This term refers to the warm periods within ice ages; we're in one of those periods now", 'value': 500, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:56.139Z', 'updated_at': '2014-02-11T22:57:56.139Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}},{'id': 14234, 'answer': 'intelligence quotient', 'question': 'You may not need a high IQ to know IQ stands for this', 'value': 200, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.698Z', 'updated_at': '2014-02-11T22:54:33.698Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}},{'id': 13607, 'answer': 'Venus', 'question': 'After the sun & moon, this planet is the brightest object in the sky', 'value': 300, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.181Z', 'updated_at': '2014-02-11T22:54:15.181Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}]

    # clues = [{'id': 20372, 'answer': 'interglacial', 'question': "This term refers to the warm periods within ice ages; we're in one of those periods now", 'value': 500, 'airdate': '1996-10-03T12:00:00.000Z', 'created_at': '2014-02-11T22:57:56.139Z', 'updated_at': '2014-02-11T22:57:56.139Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}},{'id': 14234, 'answer': 'intelligence quotient', 'question': 'You may not need a high IQ to know IQ stands for this', 'value': 200, 'airdate': '1996-01-18T12:00:00.000Z', 'created_at': '2014-02-11T22:54:33.698Z', 'updated_at': '2014-02-11T22:54:33.698Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}},{'id': 13607, 'answer': 'Venus', 'question': 'After the sun & moon, this planet is the brightest object in the sky', 'value': 500, 'airdate': '1996-04-10T12:00:00.000Z', 'created_at': '2014-02-11T22:54:15.181Z', 'updated_at': '2014-02-11T22:54:15.181Z', 'category_id': 25, 'game_id': None, 'invalid_count': None, 'category': {'id': 25, 'title': 'science', 'created_at': '2014-02-11T22:47:21.788Z', 'updated_at': '2014-02-11T22:47:21.788Z', 'clues_count': 250}}]

    ascending_order = True
    unique_values = True

    expected_output_ascending_order = True
    expected_output_unique_values = True

    values = []
    previous_val = 0
    for clue in clues:
        current_val = clue['value']

        if (current_val<=previous_val):
            ascending_order = False

        previous_val = current_val

        if (current_val in values):
            unique_values = False
        else:
            values.append(current_val)

        if(ascending_order==False and unique_values==False):
            break

    print('Values in ascending order?: ',ascending_order)
    print('Unique values?: ',unique_values)

    status = 'fail'
    if (ascending_order==expected_output_ascending_order and unique_values==expected_output_unique_values):
        status = 'pass'

    print('Status: '+status)


#TESTING USER INPUT COLLECTION

#Test 1: Check that calling check_input() with 'Q'
#results in STATE=QUIT and proper output message
def collection_2_test_1():

    print_opener('collection_2_test_1', 'Check that calling check_input() with \'Q\' results in STATE=QUIT and proper output message')

    expected_output_message = 'Thanks for playing!'
    expected_output_state = mini_jeopardy.QUIT
    actual_message = mini_jeopardy.check_input('Q',test_sorted_clues)
    actual_state = mini_jeopardy.STATE

    collection_2_print_results(expected_output_message, actual_message, expected_output_state, actual_state)

#Test 2: Check that calling check_input() with value 1
#results in STATE=CLUE_SELECTION and proper output message
def collection_2_test_2():

    print_opener('collection_2_test_2', 'Check that calling check_input() with value 1 results in STATE=CLUE_SELECTION and proper output message')

    expected_output_message = 'Here is the question: '+test_sorted_clues[0]['question']
    expected_output_state = mini_jeopardy.CLUE_SELECTION
    actual_message = mini_jeopardy.check_input('1',test_sorted_clues)
    actual_state = mini_jeopardy.STATE

    collection_2_print_results(expected_output_message, actual_message, expected_output_state, actual_state)


#Test 3: Check that calling check_input() with invalid values
#results in STATE=USR_ERROR and proper output message
def collection_2_test_3():

    print_opener('collection_2_test_3', 'Check that calling check_input() with an invalid value results in STATE=USR_ERROR and proper output message')

    expected_output_message = 'Input error. Try again.'
    expected_output_state = mini_jeopardy.USR_ERROR
    actual_message = mini_jeopardy.check_input('6',test_sorted_clues)
    actual_state = mini_jeopardy.STATE

    collection_2_print_results(expected_output_message, actual_message, expected_output_state, actual_state)

def collection_2_print_results(expected_output_message, actual_message, expected_output_state, actual_state):
    print('Expected message: ',expected_output_message)
    print('Actual message: ',actual_message)
    print('Expected state: ',expected_output_state)
    print('Actual state: ',actual_state)

    status = 'fail'
    if (expected_output_message==actual_message and expected_output_state==actual_state):
        status = 'pass'

    print('Status: '+status)

def print_opener(test_name, test_description):
    print('\n',test_name, '---------------------------------------------\n')
    print(test_description, '\n')

collection_1_test_1()
collection_1_test_2()
collection_1_test_3()
collection_2_test_1()
collection_2_test_2()
collection_2_test_3()

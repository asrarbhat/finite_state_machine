class FSM:
    def __init__(self):

        # the five tuple of a finite state machine
        self.__alphabet = []
        self.__states = []
        self.__start_state = None
        self.__final_states = []
        self.__transitions = {}

        # for FSM to match our representation
        self.__valid_fsm = False  # does FSM make sense e.g if start_state is in states
        self.__consistant_fsm = True  # is this consistant with our restrictons for data types

    def build_FSM(self, alphabet=None, states=[], start_state=None, final_states=[], transitions={}):
        """
        it takes five tuples of a fsm as input,
        then calls methods to add them to our finite state machine,
        and each called method checks the consistency of the input,
        and updates the truth value of instance variable __consistant_fsm accordingly.

        PARAMETERS
        ----------

        alphabet    : an ordered list of strings
        states      : an ordered list of strings
        start_state : a string
        final_states: an ordered list of strings
        transitions : a dictionary of with key as string and value as an ordered list

        RETURNS
        ----------
        a boolean value which says if FSM vs build sucessfully


        """

        # calling methods to build varies parts of a finite state machine
        self.__add_alphabet(alphabet)
        self.__add_states(states)
        self.__add_start_states(start_state)
        self.__add_final_states(final_states)
        self.__add_transitions(transitions)

        # checking validity of machine after all parts are build
        self.__valid_fsm = self.__consistant_fsm

        return self.__valid_fsm

    def run_FSM(self, input_string):
        if not self.__valid_fsm:
            print("please build a valid finite state machine first")
            return None
        for letter in input_string:
            if letter not in self.__alphabet:
                print("enter valid input string containing only alphabets defined")
                return None
        current_state = self.__start_state
        for letter in input_string:
            print(current_state+'   '+letter)
            current_state = self.__transitions[current_state][int(letter)]

        print(current_state in self.__final_states)

    def __add_alphabet(self, data):
        for entry in data:
            if isinstance(entry, (str,)):
                self.__alphabet.append(entry)
        if len(self.__alphabet) < len(data):
            print("enter valid alphabet  ==> [list of strings]")
            self.__alphabet = []
            return False
        return True

    def __add_states(self, data):
        for entry in data:
            if isinstance(entry, (str,)):
                self.__states.append(entry)
        if len(self.__states) < len(data):
            print("enter valid name for states  ==> [list of strings]")
            self.__states = []
            return False
        return True

    def __add_start_states(self, state):
        if state in self.__states:
            self.__start_state = state
            return True
        print("the entered state is not one of the states in finite state machine")
        return False

    def __add_final_states(self, states):
        flag = 0
        for state in states:
            if state in self.__states:
                self.__final_states.append(state)
            else:
                print(
                    f"the entered state {state} is not one of the states in finite state machine")
                flag = 1
        if flag == 0:
            return True
        return False

    def __add_transitions(self, transitions):
        self.__transitions = transitions

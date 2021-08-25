from finite_state_machine import FSM
machine = FSM()

# machine description of FSM that accepts string with odd number of ones
alphabet = ['0', '1']
states = ["first", "second"]
start_state = "first"
final_states = ["second"]
transitions = {
    "first": ["first", "second"],
    "second": ["second", "first"]
}


machine.build_FSM(alphabet, states, start_state, final_states, transitions)
machine.run_FSM("01010101")

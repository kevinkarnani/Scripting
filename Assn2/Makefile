######  Python  ###########
# if you did this in Python, single file, register
# Taken from Kurt's sample file, few edits made

PYTHON = python3
PAGER = less
my_script = assn4
state_file = state.json
test_script = test.script

.PHONY : build view clean test

build : $(my_script) $(test_script)
	@# "Not much to do here. I did this in Python"
	chmod +x $<
	chmod +x $(test_script)

view : $(my_script)
	@$(PAGER) $<

clean :
	@-\rm -rf *.pyc
	@-\rm -rf __pycache__

test : build $(state_file)
	@# "The state file needs to be deleted."
	@-\rm -rf $(state_file)

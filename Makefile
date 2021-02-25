
SRCS := $(wildcard src/*.py)
INPUTS := $(wildcard inputs/*.txt)
OUTPUTS := $(patsubst inputs%,outputs%,$(INPUTS))
$(warning $(OUTPUTS))

ARCHIVE := code.zip

.PHONY: all
all: code.zip $(OUTPUTS)

outputs/%.txt: inputs/%.txt $(SRCS)
	python3 src/simulation.py $< outputs

code.zip: $(SRCS)
	zip -r $@ $?

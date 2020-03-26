REQUIREMENTS=requirements.txt
ENV=env
env:
	virtualenv -p python3 $@
	$(MAKE) pip_install REQUIREMENTS=$(REQUIREMENTS)

pip_install:
	env/bin/pip install -r $(REQUIREMENTS)

clean_env:
	rm -rdf $(ENV)

pip_freeze:
	env/bin/pip freeze > $(REQUIREMENTS)

update_requirements:
	$(MAKE) pip_freeze
	$(MAKE) pip_install REQUIREMENTS=$(REQUIREMENTS)
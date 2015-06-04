
def new_section(concept_title, concept_description):
    html_a = '''
        <div class="concept">
            <div class="concept-title">
	         <h3>''' + concept_title + '</h3>'
    html_b=    '''          
			</div>
            <div class="concept-description">
                <p>
                 ''' + concept_description
    html_c='''
                </p>
            </div>
		</div>'''
    full_html = html_a + html_b + html_c
    return full_html

def create_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return new_section(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['test title 1', 'test description 1'],
                             ['test title 2', 'test description 2'],
                             ['test title 3', 'test description 3']] 

def create_HTML_for_list_of_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        new_HTML = create_HTML(concept)
        HTML += new_HTML
    return HTML

    
print create_HTML_for_list_of_concepts(EXAMPLE_LIST_OF_CONCEPTS)
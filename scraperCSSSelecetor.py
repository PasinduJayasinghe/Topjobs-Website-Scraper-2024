from requests_html import HTMLSession

s=HTMLSession()

r=s.get('https://www.topjobs.lk/applicant/vacancybyfunctionalarea.jsp;jsessionid=AUtNYsH7VTmGvvqCPNucmeI8?FA=SDQ')

selector='#tr0 > td:nth-child(1)'

elements = r.html.find()

for element in elements:
    print(element.text)
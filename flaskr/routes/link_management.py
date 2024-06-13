from flask import render_template, session, redirect, request
from flaskr.app import app
from flaskr.services.link_services import count_short_link, count_url, count_phishing_link, get_link_list_paginate, \
    search_list_paginate
from flaskr.services.user_services import user_by_id
from flaskr.utils.utils import convert_user_id_json_to_user_id


@app.route('/link_management/<int:page>', methods=['GET', 'POST'])
def link_management(page):
    if session and 'userId' in session:
        user_id_json = session['userId']
        user_id = convert_user_id_json_to_user_id(user_id_json)
        user = user_by_id(user_id)
        keyword = ''
        if request.method == 'POST':
            keyword = request.form.get('keyword')
            if keyword is not None:
                session['keyword'] = {'keyword': keyword}
            else:
                session.pop('keyword', None)
        if 'keyword' in session:
            keyword = session['keyword']['keyword']
            links = search_list_paginate(keyword, page)
        else:
            links = get_link_list_paginate(page)
        short_link_number = count_short_link()
        url_number = count_url()
        phishing_link_number = count_phishing_link()
        if user.is_administrator:
            return render_template('link_management.html', user=user, links=links, short_link_number=short_link_number,
                                   url_number=url_number, phishing_link_number=phishing_link_number, keyword=keyword)

    return redirect('/home/1')

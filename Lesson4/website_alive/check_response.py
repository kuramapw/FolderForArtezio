import website_alive.make_request as mr
def check_response(url_string):
    return(mr.make_request(url_string).status_code==200)

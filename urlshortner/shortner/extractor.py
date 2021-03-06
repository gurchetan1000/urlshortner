from .utils import *
from .final_prediction import pred

def get_features(url):
	suspicious_url=check_suspicious(url)
	shortened_url=check_shortening_services(url)
	contains_at_the_rate=check_the_rate(url)
	contains_double_slash=pos_of_double_slash(url)
	domain_name=get_domain_name(url)
	is_ip=domain_name['is_ip']
	domain_name=domain_name['domain_name']
	contains_hyphen=pos_of_hyphen(domain_name)
	https_token=check_https_token(domain_name)
	check_subdomains=get_subdomains(url)
	ip_address=get_ip_address(domain_name)
	has_https=get_https(url)
	dns_results=get_domain_reg_len(domain_name)
	age_domain=dns_results['age']
	dns_record=dns_results['dns_record']
	domain_reg_len=dns_results['reg_len']
	ports=port_check(ip_address)
	popularity=sitepopularity(domain_name)

	context={"suspicious_url":suspicious_url,"shortened_url":shortened_url,
	"contains_at_the_rate":contains_at_the_rate,"contains_double_slash":contains_double_slash,
	"contains_hyphen":contains_hyphen,"https_token":https_token,
	"check_subdomains":check_subdomains,"has_https":has_https,
	"age_domain":age_domain,"dns_record":dns_record,
	"domain_reg_len":domain_reg_len,"ports":ports,"popularity":popularity}

	my_list=[is_ip,suspicious_url,shortened_url,contains_at_the_rate,contains_double_slash,
	contains_hyphen,check_subdomains,has_https,domain_reg_len,ports,https_token,
	age_domain,dns_record,popularity]

	#print(pred(my_list))
	return my_list

#get_features("http://www.facebook.com/sahil.harjai.5")



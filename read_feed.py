#!/usr/bin/python

import os, sys, re, json
from shell_printing import *
import feedparser

FILER_TITLE_RE      = re.compile(r'(.*) - (.*) \((.*)\) \((.*)\)')
config_file_to_use  = "./rss_configs/sec_rss_config.json"

announcement_print("Opening RSS Config Feed(" + config_file_to_use + ")")

config      = json.loads(open(config_file_to_use).read())
feed_url    = str(config["RSS Feed URL"] + "&count=" + str(config["Count"]))

green_print("\nParsing RSS(" + str(feed_url) + ")")

full_data   = feedparser.parse(feed_url)
idx         = 0
for entry in full_data["entries"]:

    # Example Entry from the RSS Feed {'summary_detail': {'base': u'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=&company=&dateb=&owner=include&start=0&output=atom&count=100', 'type': u'text/html', 'value': u'<b>Filed:</b> 2014-07-15 <b>AccNo:</b> 0000012601-14-000166 <b>Size:</b> 149 KB', 'language': None}, 'updated_parsed': time.struct_time(tm_year=2014, tm_mon=7, tm_mday=15, tm_hour=19, tm_min=24, tm_sec=20, tm_wday=1, tm_yday=196, tm_isdst=0), 'links': [{'href': u'http://www.sec.gov/Archives/edgar/data/12601/000001260114000166/0000012601-14-000166-index.htm', 'type': u'text/html', 'rel': u'alternate'}], 'title': u'497K - PRINCIPAL VARIABLE CONTRACTS FUNDS INC (0000012601) (Filer)', 'tags': [{'term': u'497K', 'scheme': u'http://www.sec.gov/', 'label': u'form type'}], 'updated': u'2014-07-15T15:24:20-04:00', 'summary': u'<b>Filed:</b> 2014-07-15 <b>AccNo:</b> 0000012601-14-000166 <b>Size:</b> 149 KB', 'guidislink': False, 'title_detail': {'base': u'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=&company=&dateb=&owner=include&start=0&output=atom&count=100', 'type': u'text/plain', 'value': u'497K - PRINCIPAL VARIABLE CONTRACTS FUNDS INC (0000012601) (Filer)', 'language': None}, 'link': u'http://www.sec.gov/Archives/edgar/data/12601/000001260114000166/0000012601-14-000166-index.htm', 'id': u'urn:tag:sec.gov,2008:accession-number=0000012601-14-000166'}
    # print entry
    try:
        link            = str(entry["link"])
        title_entries   = FILER_TITLE_RE.findall(str(entry["title"]))
        form_type       = str(title_entries[0][0])
        company_name    = str(title_entries[0][1])
        cik             = str(title_entries[0][2])
        acc_number      = str(entry["id"].split("accession-number=")[1])

        new_hash    = {
                    "SEC ID"    : acc_number,
                    "Form Type" : str(form_type),
                    "Company"   : str(company_name),
                    "CIK"       : str(cik),
                    "Raw Title" : str(entry["title"]),
                    "URL"       : str(link)
        }

        green_print("Entry(" + str(idx) + ") => Data(" + json.dumps(new_hash) + ")\n")
    except Exception,e:
        red_print("ERROR: Failed to parse Entry(" + str(idx) + ") Data(" + str(entry) + ")")
    # end of try/ex

    idx += 1
# end of for all entries to read

announcement_print("Done Reading RSS Feed")
sys.exit(0)


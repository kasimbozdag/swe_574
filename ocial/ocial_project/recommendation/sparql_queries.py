import requests


def query_common_p_o(taken, course):
    if len(taken) == 0 or len(course) == 0:
        return {}
    taken_sparql_id_list = ""
    for t in taken:
        taken_sparql_id_list += " wd:" + t
    course_sparql_id_list = ""
    for t in course:
        course_sparql_id_list += " wd:" + t

    query = """SELECT ?ocount ?ocount1 ?pcount ?pcount1 ?scount ?scount1 WHERE {
      {
        SELECT (COUNT(DISTINCT ?o) AS ?ocount) (COUNT(DISTINCT ?p) AS ?pcount) (COUNT(DISTINCT *) AS ?scount) WHERE {
          VALUES ?s {""" + taken_sparql_id_list + """
          }
          ?s ?p ?o.
          VALUES ?ss {""" + course_sparql_id_list + """
          }
          ?ss ?p ?o.
        }
      }
      {
        SELECT (COUNT(DISTINCT ?o) AS ?ocount1) (COUNT(DISTINCT ?p) AS ?pcount1) (COUNT(*) AS ?scount1) WHERE {
          VALUES ?s {""" + taken_sparql_id_list + course_sparql_id_list + """
          }
          ?s ?p ?o.
        }
      }
    }"""
    url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?format=json&query=" + query
    res = requests.get(url)
    r = res.json()
    results = {}
    for var in r["head"]["vars"]:
        results[var] = int(r["results"]["bindings"][0][var]["value"])
        if not "1" in var:
            results[var + "_ratio"] = int(r["results"]["bindings"][0][var]["value"]) / int(r["results"]["bindings"][0][var + "1"]["value"])

    return results


def query_most_common_p_s(taken, course):
    if len(taken) == 0 or len(course) == 0:
        return {}

    taken_sparql_id_list = ""
    for t in taken:
        taken_sparql_id_list += " wd:" + t
    course_sparql_id_list = ""
    for t in course:
        course_sparql_id_list += " wd:" + t
    query = """
    SELECT ?ocount ?ocount1 ?pcount ?pcount1 ?scount ?scount1 WHERE {
      {
        SELECT (COUNT(DISTINCT ?o) AS ?ocount) (COUNT(DISTINCT ?p) AS ?pcount) (COUNT(DISTINCT *) AS ?scount) WHERE {
          VALUES ?p {
            wdt:P31
            wdt:P571
            wdt:P159
            wdt:P856
            wdt:P17
            wdt:P154
            wdt:P1454
            wdt:P373
            wdt:P452
            wdt:P127
            wdt:P414
            wdt:P740
          }
          VALUES ?s {""" + taken_sparql_id_list + """
          }
          ?s ?p ?o.
          VALUES ?ss {""" + course_sparql_id_list + """
          }
          ?ss ?p ?o.
        }
      }
      {
        SELECT (COUNT(DISTINCT ?o) AS ?ocount1) (COUNT(DISTINCT ?p) AS ?pcount1) (COUNT(*) AS ?scount1) WHERE {
          VALUES ?p {
            wdt:P31
            wdt:P571
            wdt:P159
            wdt:P856
            wdt:P17
            wdt:P154
            wdt:P1454
            wdt:P373
            wdt:P452
            wdt:P127
            wdt:P414
            wdt:P740
          }
          VALUES ?s {""" + taken_sparql_id_list + course_sparql_id_list + """
          }
          ?s ?p ?o.
        }
      }
    }
    """
    url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?format=json&query=" + query
    res = requests.get(url)
    r = res.json()
    results = {}
    for var in r["head"]["vars"]:
        results[var] = int(r["results"]["bindings"][0][var]["value"])
        if not "1" in var:
            results[var + "_ratio"] = int(r["results"]["bindings"][0][var]["value"]) / int(r["results"]["bindings"][0][var + "1"]["value"])

    return results


def query_instance_of(id_list):
    if len(id_list) == 0:
        return {}
    sparql_id_list = ""
    for t in id_list:
        sparql_id_list += " wd:" + t
    query = """
    SELECT DISTINCT ?b WHERE {
      VALUES ?s {""" + sparql_id_list + """
      }
      ?s wdt:P31 ?x.
      ?x (wdt:P279+) ?b.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,tr". }
    }
    """
    url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?format=json&query=" + query
    res = requests.get(url)
    r = res.json()
    uris = [a["b"]["value"] for a in r["results"]["bindings"]]
    return uris


def common_instance_of(taken, course):
    if len(taken) == 0 or len(course) == 0:
        return {}
    taken_uris = query_instance_of(taken)
    course_uris = query_instance_of(course)
    common = list(set(taken_uris).intersection(course_uris))
    union = list(set(taken_uris).union(course_uris))
    return {"common": len(common), "all": len(union), "ratio": len(common) / (len(union) or 1), "taken": len(taken_uris), "course": len(course_uris)}

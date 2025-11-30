#!/usr/bin/env python3
"""Module that returns top students by average score"""

def top_students(mongo_collection):
    """Return all students sorted by average score"""
    top_list = []

    for student in mongo_collection.find():
        scores = [topic['score'] for topic in student.get('topics', [])]
        average = sum(scores) / len(scores) if scores else 0
        student['averageScore'] = average
        top_list.append(student)

    return sorted(top_list, key=lambda x: x['averageScore'], reverse=True)

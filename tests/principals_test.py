from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B

def test_list_teachers(client, h_principal):
    response = client.get('/principal/teachers', headers=h_principal)

    assert response.status_code == 200

    data = response.json['data']
    assert isinstance(data, list)

    expected_number_of_teachers = 2
    assert len(data) == expected_number_of_teachers

    for teacher in data:
        assert 'id' in teacher  
        assert 'user_id' in teacher 

def test_list_all_assignments_count(client, h_principal):
    """
    Test that the correct number of assignments are returned for a principal.
    """
    response = client.get(
        '/principal/allassignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']

    assert len(data) == 5

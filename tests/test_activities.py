from src.app import activities


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_participant = "michael@mergington.edu"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in data
    assert expected_participant in data[expected_activity]["participants"]
    assert data[expected_activity]["max_participants"] == 12


def test_signup_for_activity_adds_participant(client):
    # Arrange
    activity_name = "Programming Class"
    new_student = "newstudent@mergington.edu"
    assert new_student not in activities[activity_name]["participants"]

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": new_student},
    )
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data["message"] == f"Signed up {new_student} for {activity_name}"
    assert new_student in activities[activity_name]["participants"]


def test_signup_for_nonexistent_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Club"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": "someone@mergington.edu"},
    )
    data = response.json()

    # Assert
    assert response.status_code == 404
    assert data["detail"] == "Activity not found"

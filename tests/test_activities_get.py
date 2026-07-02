def test_get_activities_returns_expected_shape(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    chess_club = payload["Chess Club"]
    assert set(["description", "schedule", "max_participants", "participants"]).issubset(chess_club.keys())
    assert isinstance(chess_club["participants"], list)

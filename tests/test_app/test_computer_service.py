import pytest
from app.services.computer_service import ComputerService


@pytest.mark.usefixtures("computers")
class TestComputer:

    @pytest.mark.development
    def test_create_computer_from_json(self, computers):
        new_computer_id = ComputerService().insert_computer_db(computers)
        expected_result = ComputerService.read_instance(new_computer_id)

        # If expected_results exists, that means there is inserted instance in data_base
        assert expected_result


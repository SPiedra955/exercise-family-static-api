"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generateId(self):
        generate_id = self._next_id
        self._next_id += 1
        return generate_id

    def add_member(self, member):
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
        for element in self._members:
            if element['id'] == id:
                self._members.remove(element)
                break
        return self._members

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

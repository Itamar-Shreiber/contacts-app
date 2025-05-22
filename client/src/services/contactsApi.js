import axios from 'axios';

const BASE_URL = 'http://localhost:5000/contacts';

export const getAllContacts = async () => {
  const res = await axios.get(BASE_URL);
  return res.data;
};

export const addContact = async (contact) => {
  return await axios.post(`${BASE_URL}/`, contact);
};

export const updateContact = async (id, contact) => {
  return await axios.put(`${BASE_URL}/${id}`, contact);
};

export const deleteContactById = async (id) => {
  return await axios.delete(`${BASE_URL}/${id}`);
};

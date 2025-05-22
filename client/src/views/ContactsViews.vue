<template>
  <div class="container">
    <div class="header-row">
      <h1>רשימת אנשי קשר</h1>
      <button class="add-button" @click="openAddForm">➕ הוסף איש קשר</button>
    </div>

    <ContactsTable :contacts="contacts" @edit="openEditForm" @delete="deleteContact" />

    <ContactForm v-if="showForm" :contact="selectedContact" @close="closeForm" @saved="handleSaved" />
  </div>
</template>

<script>
import ContactsTable from '../components/ContactsTable.vue';
import ContactForm from '../components/ContactForm.vue';
import { getAllContacts, deleteContactById } from '../services/contactsApi.js';

export default {
  components: { ContactsTable, ContactForm },
  data() {
    return {
      contacts: [],
      showForm: false,
      selectedContact: null,
    };
  },
  methods: {
    async fetchContacts() {
      this.contacts = await getAllContacts();
    },
    openAddForm() {
      this.selectedContact = null;
      this.showForm = true;
    },
    openEditForm(contact) {
      this.selectedContact = { ...contact };
      this.showForm = true;
    },
    closeForm() {
      this.showForm = false;
      this.selectedContact = null;
    },
    async handleSaved() {
      this.closeForm();
      await this.fetchContacts();
    },
    async deleteContact(id) {
      await deleteContactById(id);
      await this.fetchContacts();
    }
  },
  mounted() {
    this.fetchContacts();
  }
};
</script>
<style scoped>
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  direction: rtl;
}

.header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

h1 {
  margin: 0;
  color: #4caf50;
}

.add-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-button:hover {
  background-color: #388e3c;
}
</style>

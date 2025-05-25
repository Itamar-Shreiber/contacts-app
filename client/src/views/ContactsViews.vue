<template>
  <div class="page-wrapper">
    <div class="container">
      <div class="header-row">
        <h1>רשימת אנשי קשר</h1>
        <button class="add-button" @click="openAddForm">➕ הוסף איש קשר</button>
      </div>

      <div class="filter-row">
        <ContactsFilter ref="filterComp" @filter="handleFilter" />
        <div class="filter-actions">
          <button @click="clearFilter" class="clear-button">🧹 נקה חיפוש</button>
          <button @click="toggleSort" class="sort-button">
            {{ isSorted ? '🔽 בטל מיון' : '🔼 מיין לפי שם' }}
          </button>
        </div>
      </div>

      <ContactsTable
        :contacts="filteredContacts"
        @edit="openEditForm"
        @delete="deleteContact"
      />
      <ContactForm
        v-if="showForm"
        :contact="selectedContact"
        @close="closeForm"
        @saved="handleSaved"
      />
    </div>
  </div>
</template>

<script>
import ContactsTable from '../components/ContactsTable.vue';
import ContactForm from '../components/ContactForm.vue';
import ContactsFilter from '../components/ContactsFilter.vue';
import { getAllContacts, deleteContactById } from '../services/contactsApi.js';

export default {
  components: { ContactsTable, ContactForm, ContactsFilter },
  data() {
    return {
      contacts: [],
      filteredContacts: [],
      showForm: false,
      selectedContact: null,
      isSorted: false,
      currentQuery: '', // 🆕 נשמור את החיפוש הנוכחי
    };
  },
  methods: {
    async fetchContacts() {
      const all = await getAllContacts();
      this.contacts = all;
      this.filteredContacts = all;
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
    },
    handleFilter(query) {
      this.currentQuery = query;
      const q = query.toLowerCase();
      let filtered = this.contacts.filter(c =>
        `${c.first_name} ${c.last_name}`.toLowerCase().includes(q) ||
        (c.email && c.email.toLowerCase().includes(q)) ||
        (c.phone && c.phone.includes(q))
      );

      if (this.isSorted) {
        filtered = this.sortContacts(filtered);
      }

      this.filteredContacts = filtered;
    },
    clearFilter() {
      this.$refs.filterComp.clear(); // 🆕 מנקה את ה־input
      this.currentQuery = '';
      this.filteredContacts = this.isSorted
        ? this.sortContacts([...this.contacts])
        : [...this.contacts];
    },
    toggleSort() {
      this.isSorted = !this.isSorted;
      const baseList = this.currentQuery
        ? this.contacts.filter(c =>
            `${c.first_name} ${c.last_name}`.toLowerCase().includes(this.currentQuery.toLowerCase()) ||
            (c.email && c.email.toLowerCase().includes(this.currentQuery.toLowerCase())) ||
            (c.phone && c.phone.includes(this.currentQuery))
          )
        : [...this.contacts];

      this.filteredContacts = this.isSorted
        ? this.sortContacts(baseList)
        : baseList;
    },
    sortContacts(list) {
      return [...list].sort((a, b) => {
        const nameA = a.first_name?.toLowerCase() || '';
        const nameB = b.first_name?.toLowerCase() || '';
        return nameA.localeCompare(nameB);
      });
    },
  },
  mounted() {
    this.fetchContacts();
  },
};
</script>

<style scoped>
.page-wrapper {
  display: flex;
  justify-content: flex-end;
  direction: rtl;
  width: 100vw;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  min-height: 100vh;
}

.container {
  max-width: 1000px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  text-align: right;
  direction: rtl;
  font-family: 'Arial', sans-serif;
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

.filter-row {
  margin-bottom: 20px;
  direction: rtl;
}

.filter-actions {
  margin-top: 10px;
  display: flex;
  gap: 10px;
}

.clear-button,
.sort-button {
  padding: 8px 16px;
  font-size: 14px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background-color: #e0e0e0;
  color: #333;
  transition: background-color 0.3s ease;
}

.clear-button:hover,
.sort-button:hover {
  background-color: #ccc;
}
</style>

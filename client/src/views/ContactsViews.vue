<template>
  <div class="page-wrapper">
    <div class="container">
      <div class="header-row">
        <h1>רשימת אנשי קשר</h1>
        <button class="button button-primary" @click="openAddForm">➕ הוסף איש קשר</button>
      </div>

      <div class="filter-row">
        <ContactsFilter ref="filterComp" @filter="handleFilter" />
        <div class="filter-actions">
          <button class="button button-default" @click="clearFilter">🧹 נקה חיפוש</button>
          <button class="button button-secondary" @click="toggleSort">
          {{ isSorted ? '🔽 בטל מיון' : '🔼 מיין לפי שם' }}
        </button>
        </div>
      </div>

      <div class="contacts-table-wrapper">
        <ContactsTable
          :contacts="filteredContacts"
          @edit="openEditForm"
          @delete="deleteContact"
        />
      </div>

      <div v-if="showForm" class="contact-form-wrapper">
        <ContactForm
          :contact="selectedContact"
          @close="closeForm"
          @saved="handleSaved"
        />
      </div>
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
      currentQuery: '',
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
      this.$refs.filterComp.clear();
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
  padding: 2rem 1rem;
}

.container {
  max-width: 900px;
  margin: 0 auto;
}

.header-row,
.filter-row,
.contacts-table-wrapper,
.contact-form-wrapper {
  margin-bottom: 2rem;
}

.add-button {
  background-color: var(--color-primary, #4caf50);
  color: white;
  border: none;
  padding: 0.5em 1em;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 1rem;
  margin-left: 1rem;
}

.add-button:hover {
  background-color: var(--color-primary-dark, #388e3c);
}

.filter-actions {
  margin-top: 0.5rem;
  display: flex;
  gap: 1rem;
}

.clear-button,
.sort-button {
  background-color: var(--color-primary, #4caf50);
  color: white;
  border: none;
  padding: 0.4em 0.8em;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.3s;
}

.clear-button:hover,
.sort-button:hover {
  background-color: var(--color-primary-dark, #388e3c);
}
</style>

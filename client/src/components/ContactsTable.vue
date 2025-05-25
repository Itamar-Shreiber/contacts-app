<template>
  <div class="table-wrapper">
    <table class="contacts-table">
      <thead>
        <tr>
          <th>שם פרטי</th>
          <th>שם משפחה</th>
          <th>אימייל</th>
          <th>טלפון</th>
          <th>פעולות</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="contact in contacts" :key="contact.id">
          <td>{{ contact.first_name }}</td>
          <td>{{ contact.last_name }}</td>
          <td>{{ contact.email }}</td>
          <td>{{ contact.phone }}</td>
          <td class="action-buttons">
            <button class="button button-secondary" @click="$emit('edit', contact)">✏️ ערוך</button>
            <button class="button button-danger" @click="$emit('delete', contact.id)">🗑️ מחק</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: ['contacts']
}
</script>

<style scoped>
.table-wrapper {
  width: 100%;
  overflow-x: auto;
  direction: rtl;
}

.contacts-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0 10px; /* ריווח בין שורות */
  font-family: var(--font-base);
  color: var(--color-text);
}

.contacts-table th,
.contacts-table td {
  padding: 12px 16px;
  text-align: right;
  background-color: var(--color-background-soft);
  border-bottom: 1px solid var(--color-border);
}

.contacts-table th {
  background-color: var(--color-background-mute);
  color: var(--color-heading);
  font-weight: bold;
}

.contacts-table tbody tr:hover {
  background-color: var(--color-background-mute);
}

.action-buttons {
  display: flex;
  gap: 8px;
}
</style>

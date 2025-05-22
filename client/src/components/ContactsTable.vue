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
          <td>
            <button class="btn edit" @click="$emit('edit', contact)">✏️ ערוך</button>
            <button class="btn delete" @click="$emit('delete', contact.id)">🗑️ מחק</button>
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
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  /* מרכז כמעט לגמרי אנכית */
  padding: 20px;
  box-sizing: border-box;
}

.contacts-table {
  width: 100%;
  max-width: 900px;
  border-collapse: collapse;
  font-family: 'Arial', sans-serif;
  direction: rtl;
  text-align: right;
  margin: auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
  background-color: white;
}

.contacts-table thead tr {
  background-color: #4caf50;
  color: white;
}

.contacts-table th,
.contacts-table td {
  padding: 12px 15px;
  border-bottom: 1px solid #ddd;
}

.contacts-table tbody tr:hover {
  background-color: #f1f9f1;
  cursor: pointer;
}

.btn {
  border: none;
  padding: 6px 12px;
  margin: 0 4px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: white;
}

.btn.edit {
  background-color: #2196f3;
}

.btn.edit:hover {
  background-color: #1769aa;
}

.btn.delete {
  background-color: #f44336;
}

.btn.delete:hover {
  background-color: #aa2e25;
}
</style>

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

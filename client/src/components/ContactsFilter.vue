<!-- components/ContactsFilter.vue -->
<template>
  <div class="filter-wrapper">
    <input
      type="text"
      v-model="query"
      @input="emitFilter"
      placeholder="חפש לפי שם, אימייל או טלפון..."
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
    };
  },
  methods: {
    emitFilter() {
      this.$emit('filter', this.query);
    },
  },
};
</script>

<style scoped>
.filter-wrapper {
  margin-bottom: 20px;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 6px;
  border: 1px solid #ccc;
  direction: rtl;
  text-align: right;
}
</style>

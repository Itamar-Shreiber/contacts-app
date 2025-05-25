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
    clear() {
      this.query = '';
      this.emitFilter();
    }
  },
};
</script>

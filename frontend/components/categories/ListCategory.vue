<template>
  <b-table
    striped
    :data="categories"
    paginated
    paginate-position="bottom"
    aria-next-label="Next page"
    aria-previous-label="Previous page"
    aria-page-label="Page"
    aria-current-label="Current page"
    per-page="10"
  >
    <template v-slot="props">
      <b-table-column
        v-for="(column, index) in columns"
        :key="index"
        :field="column.field"
        :sortable="column.sortable"
        :label="column.label"
      >
        {{ props.row[column.field] }}
      </b-table-column>

      <b-table-column
        custom-key="actions"
        class="is-actions-cell"
        :label="$t('pages.admin.category.table.actions')"
      >
        <div class="buttons">
          <b-button
            type="is-small is-primary"
            icon-left="pencil"
            @click.prevent="loadCategory(props.row)"
          >
          </b-button>
          <b-button
            type="is-danger"
            class="button is-small"
            icon-left="trash-can-outline"
            @click.prevent="confirmRemove(props.row)"
          >
          </b-button>
        </div>
      </b-table-column>
    </template>
  </b-table>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  props: {
    checkable: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      isModalActive: false,
      checkedRows: [],
      columns: [
        {
          field: 'id',
          label: this.$t('pages.admin.category.table.id'),
          sortable: true
        },
        {
          field: 'name',
          label: this.$t('pages.admin.category.table.name'),
          sortable: true
        }
      ]
    }
  },
  computed: {
    ...mapState('categories', ['categories'])
  },
  created() {
    this.getCategories()
  },
  methods: {
    ...mapActions('categories', ['getCategories']),
    loadCategory(category) {
      this.$emit('loadCategory', category)
    },
    confirmRemove(category) {
      this.$buefy.dialog.confirm({
        title: 'Delete Category?',
        message:
          'Are you sure to <b>delete</b> this category? This action cannot be undone.',
        confirmText: 'Delete',
        cancelText: 'Cancel',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(category)
      })
    },
    async remove(category) {
      const id = category.id
      const url = `/api/v1/categories/${id}`
      try {
        await this.$axios.delete(url)
        this.$toasted.global.defaultSuccess()
        this.getCategories()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    }
  }
}
</script>

<style></style>

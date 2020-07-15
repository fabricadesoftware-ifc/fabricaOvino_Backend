<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Grupos</strong>
    </div>
    <div class="tile is-child is-9 groups">
      <div class="select-groups">
        <b-field>
          <b-select
            v-model="selectGroupFrom"
            multiple
            size="10"
            native-size="10"
          >
            <option
              v-for="group in groups_from"
              :key="group.id"
              :value="group.id"
              >{{ group.name }}</option
            >
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          icon-right="arrow-right-bold-outline"
          @click="selectAllGroups"
          >Escolher todos</b-button
        >
      </div>
      <div class="select-buttons">
        <b-button
          type="is-info"
          icon-right="arrow-right-bold-outline"
          @click="selectGroup"
        ></b-button>
        <b-button
          type="is-info"
          icon-right="arrow-left-bold-outline"
          @click="removeGroup"
        ></b-button>
      </div>
      <div class="select-groups">
        <b-field>
          <b-select v-model="selectGroupTo" multiple native-size="10">
            <option
              v-for="group in choosed_groups"
              :key="group.id"
              :value="group.id"
              >{{ group.name }}</option
            >
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          icon-right="arrow-left-bold-outline"
          @click="removeAllGroups"
          >Remover todos</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    choosedIds: {
      type: Array,
      default() {
        return []
      }
    },
    edit: {
      type: Boolean,
      default: false
    }
  },
  async fetch() {
    this.groups = await this.$axios.$get('/api/v1/groups/')
  },
  data() {
    return {
      selectGroupFrom: [],
      selectGroupTo: [],
      groups: []
    }
  },
  computed: {
    groups_from() {
      let choosed = this.choosedIds

      var groups = this.groups.filter(function (group) {
        return choosed.includes(group.id) == false
      })
      return groups
    },
    choosed_groups() {
      let choosed = this.choosedIds
      var groups = this.groups.filter(function (group) {
        return choosed.includes(group.id)
      })
      return groups
    }
  },
  methods: {
    selectGroup() {
      this.choosedIds = [...this.choosedIds, ...this.selectGroupFrom]
      this.selectGroupFrom = []
      this.$emit('update-choosed', this.choosedIds)
    },
    selectAllGroups() {
      this.choosedIds = [
        ...this.choosedIds,
        ...this.groups_from.map(({ id }) => id)
      ]
      this.selectGroupFrom = []
      this.$emit('update-choosed', this.choosedIds)
    },
    removeGroup() {
      this.choosedIds = this.choosedIds.filter(
        id => !this.selectGroupTo.includes(id)
      )
      this.selectGroupTo = []
      this.$emit('update-choosed', this.choosedIds)
    },
    removeAllGroups() {
      this.choosedIds = []
      this.selectGroupTo = []
      this.$emit('update-choosed', this.choosedIds)
    }
  }
}
</script>

<style>
.groups {
  display: flex;
  height: 400px;
}
.select-groups {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 40%;
}

.select-buttons {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin-top: 100px;
}

.select-buttons button {
  margin-bottom: 10px;
}
</style>

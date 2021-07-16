name = "experimental"
description = "a simple test pipeline"
default_task_id = "1"
tasks {
    task "1" {
        description = "test description"
        children = ["1", "2", "3"]
    }
    task "2" {
        description = "test description 1"
    }
}

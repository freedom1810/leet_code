#ifndef OF_TASK_H
#define OF_TASK_H

#include <iostream>
#include <filesystem>
#include <errno.h>

#include "base_task.h"
#include "INIReader.h"
#include "Logging.h"

#include "of_processor.hpp"
#include "snap_processor.hpp"

template <typename FrameData>
class OfTask : public BaseTask<FrameData> {
private: 
    OFProcessor of_process_;
    SnapProcessor snap_processor_;
    
public:
    OfTask(std::string task_name);
    virtual ~OfTask();
    FrameData process_data(const FrameData& data) override;
};

template <typename FrameData>
OfTask<FrameData>::OfTask(std::string task_name) 
    : BaseTask<FrameData>(task_name) 
{
    // Init of processor
    std::string of_config = this->reader_->Get("of", "config_of", "../configs/of/of_configs.json");
    this->logger_->log_info("[OfTask] Load config from {}", of_config);
    if (std::filesystem::exists(of_config)) {
        of_process_.init(of_config);
    } else {
        this->logger_->log_error("[OfTask] Config file doesn't exist");
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        raise(SIGTERM);
    }
}

template <typename FrameData>
OfTask<FrameData>::~OfTask(){}

// OfTask<FrameData>::init_of_process()
template <typename FrameData>
FrameData OfTask<FrameData>::process_data(const FrameData& data) {
    snap_processor_.snapshot(data, of_process_.rois);

    FrameData out_data = data;
    return out_data; 
}



#endif
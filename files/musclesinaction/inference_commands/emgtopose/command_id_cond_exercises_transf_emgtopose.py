import os
import pdb
subject = "Sruthi"
#exercises = os.listdir("SmallMIADataset/train/" + subject)
import time
command = 'tmux new-session -d -s my_session_clean_Running \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=0 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_Running_clean_baseline_perex \
--std False \
--threed True \
--predemg False \
--cond True \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valRunning.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_RonddeJambe \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=1 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_RonddeJambe_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valRonddeJambe.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_LegCross \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=2 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_LegCross_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valLegCross.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_LegBack \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=3 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_LegBack_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valLegBack.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_KneeKick \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=4 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_KneeKick_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valKneeKick.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_JumpingJack \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=5 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_JumpingJack_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valJumpingJack.txt" Enter'
os.system(command)
time.sleep(20)


command = 'tmux new-session -d -s my_session_clean_HookPunch \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=6 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_HookPunch_clean_baseline_perex \
--std False \
--threed True \
--predemg False \
--cond True \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valHookPunch.txt" Enter'
os.system(command)
time.sleep(20)


command = 'tmux new-session -d -s my_session_clean_HighKick \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=7 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_HighKick_clean_baseline_perex \
--std False \
--cond True \
--threed True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valHighKick.txt" Enter'
os.system(command)
time.sleep(20)


command = 'tmux new-session -d -s my_session_clean_FrontPunch \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=0 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_FrontPunch_clean_baseline_perex \
--std False \
--threed True \
--predemg False \
--cond True \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valFrontPunch.txt" Enter'
os.system(command)
time.sleep(20)



command = 'tmux new-session -d -s my_session_clean_FrontKick \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=1 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_FrontKick_clean_baseline_perex \
--std False \
--threed True \
--predemg False \
--cond True \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valFrontKick.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_ElbowPunch \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=1 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_ElbowPunch_clean_baseline_perex \
--std False \
--threed True \
--predemg False \
--cond True \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valElbowPunch.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_Shuffle \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=2 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_Shuffle_clean_baseline_perex \
--std False \
--threed True \
--predemg False \
--cond True \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valShuffle.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_valSideLunges \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=3 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_SideLunges_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valSideLunges.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_valSlowSkater \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=4 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_SlowSkater_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valSlowSkater.txt" Enter'
os.system(command)
time.sleep(20)

command = 'tmux new-session -d -s my_session_clean_valSquat \; send-keys \
"conda activate /proj/vondrick4/mia/condaenvs/vibe-env2" Enter \; \
send-keys "CUDA_VISIBLE_DEVICES=5 python musclesinaction/inference_scripts/inference_id_transf_cond_exercises_emgtopose.py \
--name generalization_new_cond_Squat_clean_baseline_perex \
--std False \
--threed True \
--cond True \
--predemg False \
--resume pretrained-checkpoints/generalization_new_cond_clean_emgtopose_threed/model_100.pth \
--data_path_train musclesinaction/ablation/generalization_ID_nocond_exercises/train.txt \
--data_path_val musclesinaction/ablation/generalization_ID_nocond_exercises/valSquat.txt" Enter'
os.system(command)
time.sleep(20)

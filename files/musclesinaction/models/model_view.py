import torch

# Load the checkpoint file into a dictionary
checkpoint = torch.load(r'C:\Users\birud\OneDrive - iitgn.ac.in\github\Pose-estimation\files\musclesinaction\checkpoints\test_generalization_predemg_1frame\latestcheckpoint.pth') 
checkpoint2 = torch.load(r'C:\Users\birud\OneDrive - iitgn.ac.in\github\Pose-estimation\files\musclesinaction\pretrained-checkpoints\generalization_new_cond_clean_posetoemg\model_100.pth')

model_state_dict = checkpoint['my_model']
model_state_dict2 = checkpoint2['my_model']

# Compare keys
if model_state_dict.keys() == model_state_dict2.keys():
    # Compare values for each key
    for key in model_state_dict.keys():
        if not torch.equal(model_state_dict[key], model_state_dict2[key]):
            print("Model state dictionaries are different.")

    else:
        print("Model state dictionaries are the same.")

else:
    print("Model state dictionaries have different keys.")

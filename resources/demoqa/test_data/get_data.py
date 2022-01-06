from resources.common.utils import file_ops
from os.path import join

feta_data = {}
relative_path_from_here_to_yaml = join('data.yaml')
feta_data.update(file_ops.get_yaml(__file__, relative_path_from_here_to_yaml))
relative_path_from_here_to_yaml = join('../../common/common_data/common_data.yaml')
feta_data.update(file_ops.get_yaml(__file__, relative_path_from_here_to_yaml))

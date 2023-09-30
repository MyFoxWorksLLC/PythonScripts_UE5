import unreal

#define actor locaiton
actorLocation = unreal.Vector(0, 0, 0)
actorRotation = unreal.Rotator(0, 0, 0)
levelSubsys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#create new atmosphere actors

dirLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.DirectionalLight, actorLocation, actorRotation, False)
skyLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyLight, actorLocation , actorRotation, False)
sky = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyAtmosphere, actorLocation, actorRotation, False)
fog = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.ExponentialHeightFog, actorLocation, actorRotation, False)
Clouds = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.VolumetricCloud, actorLocation, actorRotation, False)

#save level with atmospherics
levelSubsys.save_current_level()


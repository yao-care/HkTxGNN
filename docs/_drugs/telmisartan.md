---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 854
evidence_level: L5
indication_count: 9
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Telmisartan：預測新適應症為變異型心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：香港許可證資料未提供適應症文字"
---

# Telmisartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Telmisartan：從高血壓與腦中風到變異型心絞痛 (Prinzmetal angina)
{: .text-alpha }

## 一句話總結

Telmisartan 是血管收縮素受體阻斷劑，知識圖譜記錄的相關用途包括高血壓與腦中風、腦梗塞。
TxGNN 模型預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未提供適應症文字；知識圖譜記錄的相關疾病為高血壓、腦中風、腦血管疾病、腦梗塞（此為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 31 張／共 31 張） |
| 許可證數 | 31 張（有效 31 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Telmisartan 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「血管收縮素 II 係在血管收縮素轉化酶（ACE，kininase II）催化之反應中由血管收縮素 I 形成。血管收縮素 II 為腎素-血管收縮素系統之主要升壓物質，其作用包括血管收縮、刺激醛固酮之合成與釋放、心臟刺激及腎臟對鈉之再吸收。[…] Telmisartan 藉由選擇性阻斷血管收縮素 II 與許多組織（如血管平滑肌及腎上腺）中 AT 1 受體之結合，阻斷血管收縮素 II 之血管收縮作用及促醛固酮分泌作用。」英文原文："Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the reninangiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Telmisartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland."（[DailyMed: telmisartan prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56a72ddf-c2a2-45ce-91b1-1fcfbff52c10)，版本日期 2026-11-02；查閱日期 2026-11-19）。Telmisartan 屬於血管收縮素 II 第一型受體 (AT1) 阻斷劑，這是藥物類別層面的一般認知，並非本次彙整資料提供的機轉內容。

變異型心絞痛的病理與冠狀動脈血管痙攣、血管內皮功能異常有關。血管收縮素 II 會促進血管收縮，阻斷此路徑在理論上可能有幫助。另有推測認為 telmisartan 的部分 PPARγ 作用可能對血管有益。

以上都只是機轉上的合理推論。本次彙整的資料中沒有針對此疾病的臨床試驗或文獻，因此這個預測仍屬假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 31 張含本藥成分的許可證（全部有效；單一成分 18 張、複方 13 張）。以下列出 5 張單方製劑的主要許可證，仿單適應症文字與劑型欄位資料缺漏。

<!-- review:begin hk-lic-20261117-telmisartan-1 -->

> **查核更正（2026-11-17）**：原文為「本次彙整的許可證清單共 20 張，可能並非全部。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 31 張含本藥成分的許可證（全部有效；單一成分 18 張、複方 13 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-telmisartan-1 -->

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-45841 | MICARDIS TAB 40MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-45842 | MICARDIS TAB 80MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-63206 | TELMOTENS TABLETS 80MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-66969 | MICAVID TABLETS 40MG | HOVID LIMITED |
| HK-61881 | TELMISARTAN SANDOZ TABLETS 40MG | SANDOZ HONG KONG LIMITED |

清單中另有含 telmisartan 的複方製劑（如 TWYNSTA、Telmisartan Plus HCT），其資料不用於描述單方藥物的核准狀況。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，非仿單內容）：肝衰竭、腎臟疾病、胰臟炎、肝病、膽囊疾病、全身性紅斑性狼瘡、缺鉀、糖尿病、糖尿病酮酸中毒、低血壓、副甲狀腺機能亢進、肝性昏迷、肝性腦病變、無尿、痛風、高鈣血症、腎鈣質沉著症、腎動脈阻塞、膽汁淤積等。
- **藥物交互作用**（共查得 100 筆，列出主要者）：
  - 重度：檸檬酸鉀、碳酸氫鉀（合併使用可能有高血鉀風險）。
  - 中度：氫皮質酮、地塞米松、倍他米松、布地奈德、曲安奈德等皮質類固醇，以及阿斯匹靈、嗎啡、安非他酮、卡格列淨、達格列淨、恩帕列淨、艾塞那肽、人類胰島素等。

完整警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（0.9998），但沒有任何直接針對變異型心絞痛的臨床試驗或文獻，證據等級僅為 L5。

**若要推進需要：**
- 搜尋並評估 telmisartan 或同類藥物用於冠狀動脈痙攣、變異型心絞痛的臨床與前臨床研究。
- 取得詳細的作用機轉資料，並建立與變異型心絞痛的機轉連結。
- 取得香港仿單的警語、禁忌與適應症文字，以進行安全性篩選。
- 補充說明：同一次預測中，**顱內出血 (intracerebral hemorrhage)** 有已完成的 Phase 3 TRIDENT 試驗（n=1671）和 2026 年的 RCT 發表。但該試驗使用的是含 telmisartan 的三合一低劑量複方，無法單獨判定 telmisartan 的貢獻，可作為另行評估的方向。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本次彙整的許可證清單共 20 張，可能並非全部。」→「香港共有 31 張含本藥成分的許可證（全部有效；單一成分 1」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: telmisartan prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56a72ddf-c2a2-45ce-91b1-1fcfbff52c10) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


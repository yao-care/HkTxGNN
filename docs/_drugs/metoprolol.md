---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 578
evidence_level: L5
indication_count: 6
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-11-24
description: "Metoprolol：預測新適應症為Malignant hypertensive renal disease（證據等級 L5）。香港藥劑製品註冊：35 張（有效 33 張）"
---

# Metoprolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Metoprolol: Malignant hypertensive renal disease
{: .text-alpha }

## 一句話總結

Metoprolol 是一種 β1 選擇性乙型阻斷劑，知識圖譜記錄其與高血壓、急性冠心症、心肌梗塞等心血管疾病有關。
TxGNN 模型預測它可能對**慢性肺心症 (chronic pulmonary heart disease)** 有效，但目前沒有直接研究此疾病的試驗或文獻，證據僅停留在模型預測層級（L5）。
相關的臨床試驗與文獻多半探討的是合併 COPD 的心血管病人使用 β 阻斷劑的安全性，並非肺心症本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Malignant hypertensive renal disease |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 33 張／共 35 張） |
| 許可證數 | 35 張（有效 33 張） |
| 建議決策 | Hold |

> 說明：TxGNN 預測排名第 1 的是「惡性高血壓腎病變」（0.9991），但該疾病沒有任何試驗或文獻。本報告改以證據最多的「慢性肺心症」作為主要分析對象，其餘候選適應症見文末。

## 為什麼這個預測合理？

根據美國 FDA 核准的 Metoprolol 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Metoprolol 是一種β1選擇性（心臟選擇性）腎上腺素受體阻斷劑。然而，此優先作用並非絕對，在較高血漿濃度下，metoprolol 亦會抑制主要位於支氣管及血管肌肉組織的β2腎上腺素受體。」英文原文："Metoprolol is a beta 1 -selective (cardioselective) adrenergic receptor blocking agent. This preferential effect is not absolute, however, and at higher plasma concentrations, metoprolol also inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature."（[DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a)，版本日期 2026-03-03；查閱日期 2026-11-19）。根據已知資訊，metoprolol 屬於 β1 選擇性乙型阻斷劑，可降低心率、心輸出量與腎素釋放，已用於多種心血管疾病。

慢性肺心症是肺部疾病導致右心結構與功能改變的狀態，常與 COPD 並存。臨床上相關的問題是：心臟選擇性 β 阻斷劑能否在合併肺部疾病的病人中安全使用，以及是否有益。β1 選擇性理論上可減少支氣管收縮，部分觀察性研究顯示可能有益。

不過證據並不一致。以 metoprolol 治療 COPD 的 BLOCK-COPD 試驗（NCT02587351）提前終止，且後續文獻指出 metoprolol 未降低 COPD 急性惡化，反而增加需住院的惡化。因此這個預測在機轉上有討論空間，但臨床支持薄弱，且有安全疑慮。

## 臨床試驗證據

以下試驗皆針對 COPD 或相關心肺族群，並未直接以慢性肺心症為研究對象。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | 尚未招募 | 311 | 評估 metoprolol 用於射血分數降低心衰竭合併 COPD 病人，主要觀察全因死亡與再住院；尚無結果 |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | 已終止 | 532 | 以 metoprolol 預防 COPD 急性惡化的隨機、雙盲、安慰劑對照試驗；提前終止 |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | 已撤回 | 0 | 比較 carvedilol 與 metoprolol 對心衰竭病人呼吸道的影響；未收案，無證據價值 |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Early Phase 1 | 已終止 | 14 | 新冠後運動性呼吸困難合併心搏過速的治療研究；與肺心症僅間接相關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | 探討心肌梗塞且射血分數正常者使用 β 阻斷劑的效益（與肺心症無直接關係） |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | Bisoprolol 用於高惡化風險 COPD 病人；文中提到先前 metoprolol 試驗未降低惡化且住院性惡化增加 |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | 丹麥登記資料，比較 metoprolol 與 carvedilol 用於合併心衰竭、COPD、糖尿病、腎衰竭的高齡病人 |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | 台灣全國資料，評估 β 阻斷劑對心衰竭合併 COPD 病人存活的影響 |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | 世代研究 | Eur J Heart Fail | 比較心衰竭合併 COPD 病人使用 carvedilol 與 metoprolol/bisoprolol/nebivolol 的住院風險 |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Cohort | Ann Am Thorac Soc | BLOCK COPD 次分析，探討變時指數與 COPD 急性惡化及 metoprolol 不良反應的關係 |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Review | Expert Rev Respir Med | 提出 COPD 使用 β 阻斷劑的實務建議，認為仍有使用不足的情形 |
| [15358010](https://pubmed.ncbi.nlm.nih.gov/15358010/) | 2004 | Review | J Am Coll Cardiol | 討論合併 COPD 與慢性心衰竭時，非選擇性 β 與 α 阻斷的治療 |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | 臨床研究 | Heart Vessels | 50 位冠心病合併 COPD 病人使用 metoprolol，評估 β1 選擇性阻斷劑的安全性 |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | 臨床研究 | Clin Cardiol | 6 位可逆性氣道阻塞病人使用 metoprolol 200 mg/日，評估心肺功能 |

## 香港上市資訊

以下為已列出的主要許可證（共 35 張含本藥成分的許可證，有效 33 張、已註銷 2 張，單一成分 34 張、複方 1 張）。資料中未提供劑型與核准適應症文字。

<!-- review:begin hk-lic-20261117-metoprolol-1 -->

> **查核更正（2026-11-17）**：原文為「以下為已列出的主要許可證（總數至少 20 張，清單可能不完整）。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 35 張含本藥成分的許可證（有效 33 張、已註銷 2 張；單一成分 34 張、複方 1 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-metoprolol-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-63791 | METRACIN PROLONGED-RELEASE TABLETS 25MG | 單一成分 | CEUTICAL TRADING COMPANY LIMITED | 有效 |
| HK-41198 | SLOW-METOPROLOL TAB 50MG | 單一成分 | VICKMANS LABORATORIES LTD | 有效 |
| HK-65191 | METOPROLOL KRKA PROLONGED-RELEASE TABLETS 25MG | 單一成分 | SINO PACIFIC PHARMA COMPANY LIMITED | 有效 |
| HK-19885 | BETALOC IV INJ IMG/ML | 單一成分 | ASTRAZENECA HONG KONG LIMITED | 有效 |
| HK-19220 | BETALOC TAB 50MG | 單一成分 | ASTRAZENECA HONG KONG LIMITED | 已註銷 |

上表列出其中 5 張（共 35 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：焦慮症、胰臟炎、肝病、膽囊疾病、全身性紅斑狼瘡、乾癬、糖尿病與糖尿病酮酸中毒、低血壓、痛風、重症肌無力、嗜鉻細胞瘤等。
- **藥物交互作用**：資料庫共記錄 100 筆。已列出者多為中度，例如 epinephrine、corticosteroids（hydrocortisone、dexamethasone、betamethasone、budesonide 等）、bupropion、morphine、cimetidine、atropine、canagliflozin、dapagliflozin 等；aspirin 與氧化鎂為輕度。
- **與本預測相關的風險**：BLOCK-COPD 相關資料顯示，metoprolol 可能增加 COPD 病人需住院的惡化。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接針對慢性肺心症，證據等級僅能判為 L5（模型預測）。
- 最相關的 metoprolol 試驗在 COPD 中提前終止並顯示潛在風險，現有證據不足以支持推進。

**若要推進需要：**
- 取得直接以肺心症（或右心衰竭合併肺病）為對象的臨床或觀察性研究。
- 待 NCT06825728 的結果出爐後再評估。
- 補齊作用機轉與香港仿單的警語、禁忌症資料。
- 釐清 β 阻斷劑在肺高壓與右心功能不全中的血流動力學風險。

## 其他候選預測適應症（供參考）

| 預測疾病 | TxGNN 分數 | 證據等級 | 備註 |
|---------|-----------|---------|------|
| 惡性高血壓腎病變 | 0.9991 | L5 | 無試驗與文獻；屬原有高血壓用途的延伸，且 β 阻斷劑並非此病首選 |
| 肺高壓（肺病或缺氧所致） | 0.9991 | L5 | 文獻多為 β 阻斷劑中毒、心房心搏過速與動物研究，未直接探討肺高壓；有惡化缺氧或支氣管痙攣的疑慮 |
| 肺高壓（機轉不明、多因素） | 0.9991 | L5 | 無證據；β 阻斷劑在肺動脈高壓需謹慎，因可能降低心輸出量 |
| Braddock 症候群 | 0.9989 | L5 | 罕見症候群，無證據，缺乏機轉依據 |
| 拔毛症 | 0.9905 | L5 | 無證據，缺乏機轉依據 |

> 註：肺高壓兩項雖列有文獻，但並無研究直接探討該疾病，故依規則評為 L5。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「以下為已列出的主要許可證（總數至少 20 張，清單可能不完整）。」→「以下為已列出的主要許可證（共 35 張含本藥成分的許可證，有」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


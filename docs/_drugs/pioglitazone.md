---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 701
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pioglitazone：預測新適應症為Opsismodysplasia（證據等級 L5）。原適應症：第 2 型糖尿病 (type 2 diabetes mellitus)"
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pioglitazone：從第 2 型糖尿病到 Opsismodysplasia（骨發育不良症）

## 一句話總結

Pioglitazone 是一種 PPAR-gamma 促效劑，原本用於治療第 2 型糖尿病。
TxGNN 模型預測它可能對 **Opsismodysplasia** 有效（預測分數 99.59%），但目前**沒有任何臨床試驗或文獻**支持，證據僅限於模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病 (type 2 diabetes mellitus) |
| 預測新適應症 | Opsismodysplasia |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Pioglitazone 屬於 PPAR-gamma 促效劑，可調節胰島素訊號與脂肪細胞、成骨細胞的分化。

Opsismodysplasia 是一種罕見的骨骼發育不良疾病，由 INPPL1（SHIP2）功能喪失變異引起，影響 PI3K/AKT 訊號與軟骨內骨化。從訊號路徑層面來看，兩者可能有鬆散的關聯，這或許是模型給出高分的原因。

不過，目前沒有直接的機轉或臨床證據。更重要的是，PPAR-gamma 活化與骨形成減少、骨折風險上升有關，這與骨骼發育不良症的治療方向相悖。高分僅是計算預測，不應視為療效的證據。

### 其他預測適應症（供參考）

| 排名 | 預測適應症 | 預測分數 | 證據等級 | 說明 |
|------|-----------|---------|---------|------|
| 2 | Focal stiff limb syndrome | 99.50% | L5 | 屬僵人症候群範疇，與抗 GAD65 自體免疫相關；Pioglitazone 的抗發炎作用僅為推測，無已知機轉可恢復 GABA 功能 |
| 3 | Classic stiff person syndrome | 99.50% | L5 | 常合併糖尿病，模型關聯可能來自共同的糖尿病共病；現行標準治療與 PPAR-gamma 路徑無關 |
| 4 | Thiamine-responsive dysfunction syndrome | 99.48% | L5 | 糖尿病為核心表現，關聯可能源自共同的糖尿病表型；根本缺陷為硫胺素運輸異常，以補充硫胺素與胰島素治療 |
| 5 | Drug-induced localized lipodystrophy | 99.30% | L5 | PPAR-gamma 與脂肪組織生物學有合理關聯，噻唑烷二酮類在部分脂肪失養症中有研究，結果不一；但局部藥物反應性質不同，需另行文獻回顧 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Pioglitazone 在香港共有 20 張有效許可證（皆為單一成分製劑，無已註銷者）。以下列出 5 張主要許可證，其餘許可證從略。核准適應症文字在資料中未提供。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-47884 | ACTOS TAB 30MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |
| HK-47882 | ACTOS TAB 15MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |
| HK-57967 | ZOLID TAB 45MG | CHARIOT PHARMA LIMITED |
| HK-58692 | APO-PIOGLITAZONE TAB 30MG | HIND WING CO LTD |
| HK-56745 | GLITTER-15 TAB 15MG | UNIPHARM (HONG KONG) LIMITED |

---

## 安全性考量

- **知識圖譜中的禁忌疾病（非仿單內容）**：知識圖譜顯示的禁忌或需謹慎的疾病包括腎臟疾病、肝臟疾病、膽囊疾病、充血性心衰竭、腎上腺皮質功能不全 (Addison disease)、感染性疾病，以及多種腦下垂體功能不足相關疾病（如腦下垂體功能低下、生長激素缺乏、低促性腺素性性腺功能低下、Kallmann 症候群、Sheehan 症候群）等。此為圖譜關聯，須以原廠仿單確認。
- **藥物交互作用**：資料庫共收錄 100 筆，以下為部分範例（皆為 DDInter 來源）：
  - 中度：Abiraterone、Phenylephrine、Acetazolamide、Formoterol、Pseudoephedrine、Epinephrine、Hydrocortisone、Salbutamol、Ethanol、Hydrochlorothiazide、Alpelisib
  - 輕度：Nifedipine、Ethinylestradiol、Lipoic acid、Aminoglutethimide

此外，PPAR-gamma 活化與骨折風險上升有關，對骨骼疾病的使用需特別審慎。其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有任何臨床試驗或文獻佐證。
- 機轉上 PPAR-gamma 活化可能減少骨形成並增加骨折風險，與骨骼發育不良症的治療目標相悖。

**若要推進需要：**
- 取得 Pioglitazone 的詳細作用機轉資料，並分析其與 INPPL1/SHIP2、PI3K/AKT 路徑的實際關聯
- 進行系統性文獻回顧與前臨床研究（如細胞或動物模型），驗證對骨骼與軟骨發育的影響
- 取得香港衛生署的仿單，完成警語與禁忌症的安全性篩選
- 若要評估其他預測適應症，可優先檢視 drug-induced localized lipodystrophy，因其與 PPAR-gamma 的脂肪生物學關聯相對合理
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


---
layout: default
title: Levothyroxine
parent: 僅模型預測 (L5)
nav_order: 529
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-23
description: "Levothyroxine：預測新適應症為腎發育不全／無發育 (renal hypodysplasia/aplasia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Levothyroxine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Levothyroxine: 腎發育不全／無發育 (renal hypodysplasia/aplasia)
{: .text-alpha }

## 一句話總結

Levothyroxine（左旋甲狀腺素）是合成甲狀腺素，知識圖譜中記錄的用途以甲狀腺功能低下及甲狀腺相關疾病為主。
TxGNN 模型預測它可能對**腎發育不全／無發育 (renal hypodysplasia/aplasia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測，生物學合理性偏低。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 腎發育不全／無發育 (renal hypodysplasia/aplasia) |
| TxGNN 預測分數 | 0.9967 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 核准許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Levothyroxine 是合成的甲狀腺素，一般認為甲狀腺激素訊號在腎臟發育（腎元生成、腎小管成熟）與功能維持中扮演一般性角色。

然而，腎發育不全／無發育屬於結構性的先天畸形，目前沒有證據顯示補充甲狀腺素能逆轉或治療這類器官形成異常。0.9967 的高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非真正的生物學證據。

同一批預測中的其他候選疾病（雙側腎無發育、Potter 序列、Carney 複合症）同樣沒有臨床試驗或文獻支持。其中 Carney 複合症因可能伴隨甲狀腺結節或腫瘤，與甲狀腺相關適應症有微弱的間接關聯，但仍屬假說層級。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

以下列出 5 張主要許可證，許可證資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 製造商 |
|---------|------|-------|
| HK-63576 | ELTROXIN TABLETS 50MCG | Aspen Pharmacare Asia |
| HK-56044 | LEVOTHYROXINE TAB 50MCG | Teva Pharmaceutical Hong Kong |
| HK-67851 | EUTHYROX TABLETS 100 MICROGRAMS | Merck Pharmaceutical (HK) |
| HK-57830 | OROXINE TAB 200MCG | Aspen Pharmacare Asia |
| HK-58763 | LEVOTHYROXINE TAB 50MCG | Hind Wing |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：知識圖譜記錄 Levothyroxine 與下列疾病存在禁忌關聯，包括高血壓、腦下垂體功能低下與相關缺乏症、生長激素缺乏、性腺功能低下（含 Kallmann 症候群）、胸腺疾病、骨質疏鬆（含停經後骨質疏鬆）、糖尿病及酮酸中毒、冠狀動脈疾病、心肌梗塞。
- **藥物交互作用**：資料共收錄 100 筆交互作用，以下為部分主要項目。
  - 降血糖藥物：Acarbose、Metformin、Pioglitazone、Alogliptin、Canagliflozin、Dapagliflozin、Empagliflozin、Chlorpropamide、Albiglutide、Dulaglutide（中度）
  - 制酸／降胃酸藥物：Omeprazole、Rabeprazole、Dexlansoprazole（中度）、Cimetidine（輕度）
  - 含鈣或鎂的製劑：Calcium Phosphate、Calcium acetate、Magnesium oxide（中度）
  - 擬交感神經類：Epinephrine、Isometheptene、Diethylpropion（中度）

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 四個預測適應症皆無臨床試驗與文獻支持，且機轉上缺乏合理性，高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。
- 腎發育不全屬結構性先天畸形，甲狀腺素替代無法使缺失的器官重新形成。

**若要推進需要：**
- 補齊作用機轉資料，並說明甲狀腺素訊號與腎臟發育的具體關聯
- 進行系統性文獻檢索，確認是否有任何直接研究該疾病的證據
- 取得香港仿單的警語與禁忌資料，再進行安全性篩選
- 若有前臨床證據，再重新評估是否值得推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


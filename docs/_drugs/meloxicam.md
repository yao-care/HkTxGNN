---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 559
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Meloxicam：預測新適應症為肢中型發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia…（證據等級 L5）。原適應症：類風濕性關節炎、骨關節炎、關節病變、幼年型特發性關節炎、脊椎關節病變"
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia"]
---

# Meloxicam
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

# Meloxicam：從類風濕性關節炎／骨關節炎到肢中型發育不良（Hunter-Thompson 型）

## 一句話總結

Meloxicam 是一種偏好抑制 COX-2 的非類固醇消炎止痛藥（NSAID），原本用於類風濕性關節炎、骨關節炎等關節疾病。
TxGNN 模型預測它可能對 **肢中型發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、骨關節炎、關節病變、幼年型特發性關節炎、脊椎關節病變（來自知識圖譜；許可證未載明適應症文字） |
| 預測新適應症 | 肢中型發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Meloxicam 是偏好抑制 COX-2 的 NSAID，透過減少前列腺素合成來消炎止痛，在關節疾病中的療效已被證實。

Hunter-Thompson 型肢中型發育不良是罕見的骨骼發育疾病，起因於 GDF5 (CDMP1) 功能喪失變異，影響軟骨生成與肢體生長。目前**沒有已知的機轉連結**能把 COX-2 抑制與 GDF5/BMP 訊號串起來。

這個預測較可能來自知識圖譜中「骨骼／關節表型」的網路鄰近性，而非藥理學依據。Meloxicam 頂多提供症狀性的疼痛緩解，無法改變疾病本身。

其他排名前五的預測同樣缺乏證據（皆為 L5），其中以**假性軟骨發育不全 (pseudoachondroplasia)**（分數 99.81%）生物學上最合理：此病有早發性關節痛與骨關節炎，發炎訊號在前臨床模型中也被認為有貢獻，NSAID 可能有症狀性益處，但仍屬間接推論。

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 |
|------|---------|-----------|---------|
| 1 | 肢中型發育不良，Hunter-Thompson 型 | 99.92% | L5 |
| 2 | 短椎體症—牙釉質發育不全症候群 (brachyolmia-amelogenesis imperfecta syndrome) | 99.92% | L5 |
| 3 | 肌硬化症 (myosclerosis) | 99.90% | L5 |
| 4 | 短椎體症 (brachyolmia) | 99.89% | L5 |
| 5 | 假性軟骨發育不全 (pseudoachondroplasia) | 99.81% | L5 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效許可證（皆為單方，無已註銷）。下表列出 5 張主要許可證，許可證資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-41788 | MOBIC TAB 7.5MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-41789 | MOBIC TAB 15MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-54749 | APO-MELOXICAM TAB 7.5MG | HIND WING CO LTD |
| HK-54750 | APO-MELOXICAM TAB 15MG | HIND WING CO LTD |
| HK-53980 | MOXIC FORTE TAB 15MG | HANG LUNG TRADING (H.K.) CO |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單文字）：高血壓、腎臟疾病與腎功能受損、充血性心衰竭、心肌梗塞、冠狀動脈血栓、心血管疾病、心臟病、中風與腦血管疾病、腦梗塞、活動性消化性潰瘍、胃炎、凝血疾病、貧血（含巨球性貧血）、血紅素病變、糖尿病與糖尿病酮酸中毒、高血脂與家族性高血脂、物質濫用／依賴、輸尿管積膿。
- **藥物交互作用**：共查得 100 筆，以下為部分範例，多數為中度。
  - 中度：Acetylsalicylic acid（阿斯匹靈）、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（皆為皮質類固醇）、Metformin、Glimepiride、Chlorpropamide、Mesalazine、Balsalazide、Vancomycin、Kanamycin、Aprepitant
  - 輕度：Linaclotide

其餘仿單警語與禁忌資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.92%），但無任何臨床試驗或文獻，也找不到 COX-2 抑制與 GDF5/BMP 訊號之間的機轉連結，證據等級僅 L5。
- 此疾病為遺傳性骨骼發育異常，Meloxicam 最多只能做症狀性疼痛處理，不具疾病修飾潛力；且藥物的心血管、腎臟與腸胃道禁忌風險需一併考量。

**若要推進需要：**
- 補齊 Meloxicam 的作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌資料，以進行安全性篩選
- 前臨床研究（如 GDF5 缺陷模型中的發炎或疼痛相關終點）
- 若要聚焦症狀性疼痛處理，可優先評估假性軟骨發育不全，並先建立疾病與疼痛／關節炎關聯的文獻佐證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 7
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-10-23
description: "Ibuprofen：預測新適應症為肢端中段發育不良 Hunter-Thompson 型（證據等級 L5）。原適應症：知識圖譜記錄的關聯包括類風濕性關節炎、骨關節炎、頭痛、幼年型特發性關節炎等"
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Ibuprofen：Hunter-Thompson 型肢中發育不良
{: .text-alpha }

## 一句話總結

Ibuprofen（布洛芬）是非類固醇消炎止痛藥，知識圖譜中記錄的相關用途包括類風濕性關節炎、骨關節炎、頭痛與動脈導管未閉等。
TxGNN 模型預測它可能對**肢端中段發育不良 Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯包括類風濕性關節炎、骨關節炎、頭痛、幼年型特發性關節炎等（本次整理的資料中，香港許可證未附適應症文字） |
| 預測新適應症 | 肢端中段發育不良 Hunter-Thompson 型 |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，ibuprofen 屬於非選擇性 COX 抑制劑，可提供消炎與止痛效果，但這是依藥物類別所作的說明，並非本次資料所載。

Hunter-Thompson 型肢端中段發育不良是罕見的骨骼發育異常，成因為 CDMP1/GDF5 功能喪失變異，影響軟骨發育中的 BMP 訊號。Ibuprofen 只能緩解症狀，無法矯正這類發育性基因缺陷，因此**找不到可信的機轉連結**。

0.9974 的高分來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下表僅列出 5 張許可證，總數至少 20 張，清單可能不完整。本次整理的資料中，這些許可證均未附劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55058 | INFACALM IBUPROFEN INFANT DROPS 40MG/ML | TIANDA PHARMACEUTICALS LIMITED |
| HK-43233 | BUPOGESIC 200 TAB 200MG | VICKMANS LABORATORIES LTD |
| HK-67025 | WILLIPO IBUPROFEN TABLETS 200MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-51501 | NUROFEN GEL 5%W/W | RECKITT BENCKISER HONG KONG LTD |
| HK-54601 | BRUFEN TAB 400MG | ABBOTT LAB LTD |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：高血壓、肝衰竭、腎臟疾病、肝病、消化性潰瘍、發炎性腸道疾病、血小板低下、凝血疾病、中風與腦血管疾病、心肌梗塞、癲癇、慢性阻塞性肺病、糖尿病、全身性紅斑狼瘡、甲狀腺功能低下等。
- **藥物交互作用**（共 100 筆紀錄，以下為部分）：
  - 重大：Acetylsalicylic acid（阿斯匹靈）
  - 中度：Acetohexamide、Glimepiride、Glipizide、Glyburide、Chlorpropamide 等降血糖藥；Betamethasone、Budesonide、Dexamethasone、Hydrocortisone 等類固醇；Aprepitant、Balsalazide、Exenatide、Fenfluramine、Kanamycin、Levofloxacin
  - 輕微：Famotidine、Ranitidine、Cimetidine

仿單的警語與禁忌資料尚未取得，詳細安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5，且機轉上找不到可信的連結。高預測分數來自 TxGNN 模型（深度學習），可能只反映模型在相關疾病之間學到的相似性，而非生物學證據。
- 此病為基因性發育異常，ibuprofen 至多只能緩解疼痛症狀，不屬於疾病修飾治療。

**若要推進需要：**
- 補齊作用機轉資料，並取得香港仿單的警語與禁忌內容
- 以文獻檢索確認 GDF5/BMP 相關病理與 COX 抑制之間是否有任何實證關聯
- 若僅考慮症狀性止痛用途，需另行評估其意義，並對照知識圖譜所列的禁忌族群

**補充：** 同批預測的其他疾病（brachyolmia-amelogenesis imperfecta 症候群、myosclerosis、brachyolmia、brachydactyly-syndactyly 症候群、pseudoachondroplasia、colobomatous microphthalmia-rhizomelic dysplasia 症候群）同樣沒有試驗或文獻，皆為 L5 與 Hold。其中 pseudoachondroplasia 與 myosclerosis 僅有症狀性止痛的間接可能性，其餘無可信機轉連結。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


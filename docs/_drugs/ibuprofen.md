---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ibuprofen：預測新適應症為肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia…（證據等級 L5）。原適應症：類風濕性關節炎、頭痛、骨關節炎、關節病變、幼年型特發性關節炎、脊椎關節病變、動脈導管未閉"
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome"]
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ibuprofen：從類風濕性關節炎等發炎疼痛疾病到肢端中段發育不良（Hunter-Thompson 型）

## 一句話總結

Ibuprofen 是常見的非類固醇消炎止痛藥（NSAID），原本用於類風濕性關節炎、骨關節炎、頭痛、幼年型特發性關節炎及動脈導管未閉等。
TxGNN 模型預測它可能對**肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、頭痛、骨關節炎、關節病變、幼年型特發性關節炎、脊椎關節病變、動脈導管未閉（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 肢端中段發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ibuprofen 屬於非選擇性 COX 抑制劑，透過減少前列腺素合成來發揮消炎、止痛與退燒作用，其在關節與肌肉骨骼疼痛疾病中的療效已獲證實。

此預測的疾病是一種罕見的骨骼發育不良，由 CDMP1/GDF5 功能喪失變異（BMP 訊號路徑）引起。COX 抑制與 GDF5/BMP 路徑的修復之間，目前找不到合理的機轉連結。模型分數高，較可能反映的是知識圖譜中，該疾病與 ibuprofen 已核准適應症（如關節病變、骨關節炎）在肌肉骨骼表型上的鄰近性，而非因果機轉。

就算有作用，NSAID 最多只能緩解關節疼痛等症狀，無法改變發育不良本身的病程。

其他排名前五的預測（brachyolmia-amelogenesis imperfecta syndrome、myosclerosis、brachyolmia、brachydactyly-syndactyly syndrome）分數同為約 99.7%，同樣沒有臨床試驗或文獻，機轉連結也同樣薄弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，皆為現行有效。下表列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-54601 | BRUFEN TAB 400MG | ABBOTT LAB LTD |
| HK-51501 | NUROFEN GEL 5%W/W | RECKITT BENCKISER HONG KONG LTD |
| HK-55058 | INFACALM IBUPROFEN INFANT DROPS 40MG/ML | TIANDA PHARMACEUTICALS LIMITED |
| HK-35198 | APO-IBUPROFEN TAB 200MG | HIND WING CO LTD |
| HK-50200 | SPEDIFEN GRANULES 600MG | ZENFIELDS (H.K.) LIMITED |

## 安全性考量

- **禁忌症（知識圖譜關聯，非仿單內容）**：圖譜中標示與下列疾病有禁忌關聯，主要包括：
  - 心血管與腦血管：高血壓、心肌梗塞、中風、腦梗塞、腦血管疾病
  - 肝腎：肝衰竭、肝病、腎臟病
  - 消化道：消化性潰瘍、發炎性腸病
  - 血液：血小板低下、凝血疾病
  - 其他：癲癇、慢性阻塞性肺病、糖尿病、酮酸中毒、系統性紅斑狼瘡、甲狀腺低下、缺鉀、良性前列腺增生、低血壓、物質濫用/依賴
- **藥物交互作用**：資料庫共有 100 筆交互作用紀錄，以下為其中部分：
  - **重大 (Major)**：Acetylsalicylic acid（阿斯匹靈）
  - **中度 (Moderate)**：口服降血糖藥（Acetohexamide、Chlorpropamide、Glimepiride、Glipizide、Glyburide）、類固醇（Betamethasone、Budesonide、Dexamethasone、Hydrocortisone）、Aprepitant、Balsalazide、Exenatide、Fenfluramine、Dexfenfluramine、Kanamycin、Levofloxacin
  - **輕微 (Minor)**：Famotidine、Ranitidine、Cimetidine

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。此外，這類罕見骨骼發育疾病若涉及兒童或孕期族群，NSAID 的使用須格外謹慎。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測分數（99.74%），沒有任何臨床試驗或文獻，證據等級為 L5。
- 疾病的致病機轉（GDF5/BMP 訊號缺陷）與 COX 抑制沒有可辨識的關聯，ibuprofen 最多只能緩解症狀，無法修正疾病本身。

**若要推進需要：**
- 補充 ibuprofen 的作用機轉資料，並釐清其與 GDF5/BMP 路徑是否有任何連結
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 若要作為症狀處理用途，需先有該疾病族群的疼痛或發炎相關臨床觀察資料
- 建議改以症狀緩解而非疾病修飾為目標重新評估，或轉向機轉較明確的候選藥物
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


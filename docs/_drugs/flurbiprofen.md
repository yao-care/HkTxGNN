---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Flurbiprofen：預測新適應症為Hunter-Thompson 型肢中發育不良 (Acromesomelic dysplasia…（證據等級 L5）。原適應症：類風濕性關節炎、骨關節炎、關節病變"
monitor_inn: "FLURBIPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Flurbiprofen
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

# Flurbiprofen：從類風濕性關節炎到 Hunter-Thompson 型肢中發育不良

## 一句話總結

Flurbiprofen 是一種非選擇性 COX 抑制劑（NSAID），原本用於類風濕性關節炎、骨關節炎等關節疾病。
TxGNN 模型預測它可能對 **Hunter-Thompson 型肢中發育不良 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效，但目前 **沒有任何臨床試驗或文獻**支持，僅為模型預測，且缺乏可信的機轉依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、骨關節炎、關節病變（香港許可證未載明核准適應症文字，此為知識圖譜之適應症） |
| 預測新適應症 | Hunter-Thompson 型肢中發育不良 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Flurbiprofen 屬於非選擇性 COX 抑制劑，具止痛與抗發炎作用，在關節炎類疾病中的症狀緩解效果已為人所知。

然而，Hunter-Thompson 型肢中發育不良是罕見的遺傳性骨骼發育不良，與 CDMP1/GDF5 功能喪失變異有關，這些變異會破壞軟骨與肢體發育中的 BMP 訊號傳遞。Flurbiprofen 並不作用於 GDF5/BMP 路徑，**沒有可信的機轉連結**。

極高的 TxGNN 分數（0.9999）較可能反映知識圖譜中與骨骼、關節疾病節點的鄰近性，而非藥理學上的合理性。因此這個預測應視為計算上的人為結果，而非有力的再利用線索。

其他排名前列的預測（brachydactyly-syndactyly syndrome、colobomatous microphthalmia-rhizomelic dysplasia syndrome、brachyolmia-amelogenesis imperfecta syndrome）同樣為先天發育異常，也都沒有機轉或實證支持。排名第 5 的肌硬化症 (myosclerosis) 僅有微弱且推測性的關聯：NSAID 理論上可緩解肌肉骨骼疼痛，但沒有證據顯示能改變纖維化進程。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68354 | SULAN TABLETS 100MG | 錠劑 | 未載明 |
| HK-64202 | FUKON TABLETS 50MG | 錠劑 | 未載明 |
| HK-61431 | STREPFEN HONEY & LEMON LOZENGE 8.75MG | 口含錠 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）**：高血壓、腎臟疾病、肝臟疾病、膽囊疾病、消化性潰瘍（含活動性）、物質濫用/依賴、凝血疾病、心肌梗塞、冠狀動脈血栓、血紅素病變、心血管疾病、心臟病、膿輸尿管。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：Acetylsalicylic acid（阿斯匹靈）、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（皮質類固醇類）、Metformin、Glimepiride、Chlorpropamide（降血糖藥）、Mesalazine、Balsalazide、Aprepitant
  - 輕微：Famotidine、Cimetidine、Linaclotide

其餘警語與正式禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 該疾病的致病機轉（GDF5/BMP 訊號缺陷）與 COX 抑制無關，高分很可能是圖譜鄰近性造成的假象。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並重新評估是否存在任何可信的機轉連結。
- 取得香港衛生署的仿單（警語、禁忌症與核准適應症），完成安全性篩選。
- 建議優先檢視其他預測（例如肌硬化症）是否有可驗證的症狀緩解假說，或改以原適應症為主的開發方向，而非追蹤此預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


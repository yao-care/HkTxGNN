---
layout: default
title: Metyrapone
parent: 僅模型預測 (L5)
nav_order: 580
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metyrapone：預測新適應症為運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia)（證據等級 L5）。原適應症：香港許可證未載明"
monitor_inn: "METYRAPONE"
predicted_indications: ["exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement"]
---

# Metyrapone
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

## Metyrapone：從腎上腺皮質功能檢測與庫欣氏症到運動誘發惡性高熱
{: .text-alpha }

## 一句話總結

Metyrapone 是 11-beta-hydroxylase (CYP11B1) 抑制劑，臨床上用於下視丘－腦下垂體功能診斷，也偶爾用於庫欣氏症 (Cushing's syndrome) 的治療。
TxGNN 模型預測它可能對**運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；藥理資料顯示用於下視丘－腦下垂體功能診斷及庫欣氏症 |
| 預測新適應症 | 運動誘發惡性高熱 (Exercise-induced Malignant Hyperthermia) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，metyrapone 抑制 CYP11B1（11-beta-hydroxylase）與 CYP11B2，進而減少皮質醇合成，因此用於腎上腺皮質過度分泌的診斷與治療。

惡性高熱的成因則是骨骼肌鈣離子釋放失調，多與 RYR1 基因變異有關（少數為 CACNA1S）。目前沒有已知路徑能將抑制皮質醇合成與 RYR1 介導的鈣離子調控連結起來。

因此，這個高分預測較可能來自知識圖譜中疾病之間的鄰近關係，而非生物學上的合理依據。排名前五的預測（惡性高熱易感性、King-Denborough 症候群、中央核心肌病、多小核心病）全都屬於 RYR1 相關肌病，看起來是同一個圖譜偏差的重複呈現，而非各自獨立的訊號。

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
| HK-19150 | METOPIRONE CAP 250MG | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病禁忌關聯，非仿單內容）：
  - 艾迪生氏病 (Addison disease)
  - 慢性原發性腎上腺功能不全
  - 腎上腺功能不全
  - 腎上腺皮質功能不全
  - 家族性腎上腺發育不全（合併腦下垂體黃體生成素缺乏）
  - 家族性糖皮質素缺乏症
  - X 染色體連鎖先天性腎上腺發育不全
  - 因 CYP11A1 部分缺乏所致的遺傳性單純腎上腺功能不全
  - 先天性腎上腺增生
- **藥物交互作用**：共查得 12 筆，其中 10 筆為中度交互作用，另 2 筆為藥理標靶資料（CYP11B1、CYP11B2），並非交互作用分級。
  - 雌激素類：ethinylestradiol、estradiol、conjugated estrogens、mestranol、esterified estrogens、estrone sulfate（含外用劑型）
  - cyproheptadine

其餘警語與禁忌的仿單資料目前缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（L5），沒有任何臨床試驗或文獻，且與 RYR1 相關肌病之間缺乏合理的機轉連結，排名前五的預測也彼此高度重疊。
- 此外，香港仿單的警語與禁忌資料缺失，目前無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌、適應症、劑型）
- 補齊 metyrapone 的作用機轉資料
- 提出皮質醇合成抑制與肌肉鈣離子調控之間的機轉假說，並以前臨床研究（例如 RYR1 肌肉模型）驗證
- 評估該藥在腎上腺功能不全風險下，用於肌病患者的安全性
- 若上述步驟都沒有支持性證據，建議不再往此適應症投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


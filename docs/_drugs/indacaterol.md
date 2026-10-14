---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 5
---

# Indacaterol
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

# Indacaterol：從慢性阻塞性肺病（推測）到腎因性抗利尿不適當症候群

## 一句話總結

Indacaterol 是一種超長效 β2 腎上腺素受體促效劑，香港已有多張吸入劑許可證。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，且機轉上的作用方向可能不利。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，許可證未載明核准適應症 |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Indacaterol 是超長效 β2 腎上腺素受體促效劑，以吸入粉末劑型上市，多與其他支氣管擴張劑或吸入性類固醇組成複方產品。

NSIAD 由抗利尿激素 V2 受體（AVPR2）的功能獲得性突變引起，會增加 cAMP 訊號並促使集尿管的水通道蛋白-2 插入細胞膜。β2 促效劑同樣會提高 cAMP，理論上可能**加重**水分滯留，而非改善病情。因此兩者的關聯僅屬推測，作用方向甚至可能不利。

99.54% 的高分只是模型預測，沒有試驗或文獻佐證，不宜視為療效證據。

另外四個較低排名的預測（頭痛疾患、三叉自律神經頭痛、腱鞘周圍炎、鈣化性肌腱炎）同樣只有模型預測，且機轉依據薄弱：頭痛本身就是 β2 促效劑的已知副作用，吸入給藥的全身暴露量也低，不利於肌腱疾病。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67628 | ONBREZ BREEZHALER 吸入粉末 150mcg/膠囊 | 吸入粉末膠囊 | 未載明 |
| HK-67725 | ONBREZ BREEZHALER 吸入粉末 300mcg/膠囊 | 吸入粉末膠囊 | 未載明 |
| HK-60180 | ONBREZ BREEZHALER 吸入粉末 150mcg/膠囊 | 吸入粉末膠囊 | 未載明 |
| HK-60179 | ONBREZ BREEZHALER 吸入粉末 300mcg/膠囊 | 吸入粉末膠囊 | 未載明 |
| HK-67120 | ATECTURA BREEZHALER 吸入粉末硬膠囊 150mcg/160mcg | 吸入粉末硬膠囊 | 未載明 |

以上為 13 張許可證中的 5 張，皆由 Novartis Pharmaceuticals (HK) Limited 持有，狀態皆為有效。

## 安全性考量

- **知識圖譜中的禁忌疾病關聯**（來自模型知識圖譜，非仿單內容）：高血壓、長 QT 症候群（含家族性）、癲癇、高血糖、缺鉀症、糖尿病、糖尿病酮酸中毒、心因性猝死、心臟傳導疾病、甲狀腺毒症／甲狀腺機能亢進、葛瑞夫茲氏病、冠狀動脈疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分例子。
  - 中度：Acarbose、Isometheptene、Famotidine、Epinephrine、Albiglutide、Alogliptin、Metformin、Pioglitazone、Canagliflozin、Chlorpropamide、Clarithromycin、Dapagliflozin、Saxagliptin
  - 輕度：Hydrocortisone、Aprepitant、Triamcinolone、Dexamethasone、Beclomethasone dipropionate、Betamethasone、Budesonide

  多種降血糖藥列為中度交互作用，與 β2 促效劑可能升高血糖的特性相符。

仿單的警語與禁忌症資料尚未取得，完整安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型預測（L5），沒有任何臨床試驗或文獻支持。
- 對於排名第一的 NSIAD，β2 促效劑提高 cAMP 的作用，理論上可能加重水分滯留，方向可能相反。

**若要推進需要：**
- 取得香港仿單的警語與禁忌症，完成安全性初篩。
- 補齊 Indacaterol 的作用機轉資料，釐清與 NSIAD 的機轉關聯與作用方向。
- 進行文獻與臨床試驗檢索；若仍無證據，建議不再推進這些預測。
- 若仍考慮推進，先做體外或動物的機轉驗證，確認 β2 促效劑對 AVPR2 相關 cAMP 訊號與水分排泄的影響。
- 釐清各許可證的核准適應症，以確認原適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


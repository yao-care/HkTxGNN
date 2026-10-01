---
layout: default
title: Levocetirizine
parent: 僅模型預測 (L5)
nav_order: 516
evidence_level: L5
indication_count: 3
---

# Levocetirizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Levocetirizine：從過敏性疾病到類風濕性關節炎

## 一句話總結

Levocetirizine 是 H1 受體拮抗劑（抗組織胺），香港已有多張許可證，但本次資料未提供原適應症文字。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
目前**沒有臨床試驗與文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Levocetirizine 是選擇性 H1 受體拮抗劑（反向促效劑），主要用於過敏相關症狀。

組織胺與肥大細胞被認為與類風濕性關節炎的滑膜發炎、血管新生及血管通透性增加有關，因此在生物學上有一定關聯。

但這個關聯帶有推測性：H1 阻斷並非公認的類風濕性關節炎疾病修飾機轉，現有資料也沒有支持證據。0.997 的 TxGNN 分數只是計算預測，無法代表臨床療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-68967 | LOCEMINE TABLETS 5MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-54600 | XYZAL ORAL DROPS 5MG/ML | GLAXOSMITHKLINE LIMITED |
| HK-64194 | SINUSCLEAR TABLETS 5MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-68844 | ALERIN TABLETS 5MG | SB PHARMA LIMITED |
| HK-67378 | ZYX TABLETS 5MG | WA MAN (HK) LIMITED |

## 其他較低分預測

TxGNN 另預測兩項適應症，分數同樣很高，但兩者皆無臨床試驗與文獻，也找不到與 H1 受體拮抗的合理機轉連結，建議 Hold：

| 預測適應症 | TxGNN 分數 | 評估 |
|-----------|-----------|------|
| 眼缺損性小眼症-肢根型發育不良症候群 (Colobomatous microphthalmia-rhizomelic dysplasia syndrome) | 99.59% | 極罕見的先天發育疾病，抗組織胺不太可能改變其病理，高分可能來自知識圖譜的連結假象 |
| 短指-併指症候群 (Brachydactyly-syndactyly syndrome) | 99.52% | 先天肢體畸形，屬結構性發育異常，抗組織胺預期無效，高分很可能是圖譜假象 |

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有任何臨床試驗或文獻。H1 阻斷並非類風濕性關節炎的公認機轉，目前無法評估臨床訊號。

**若要推進需要：**
- 系統性檢索類風濕性關節炎與抗組織胺（組織胺、肥大細胞、H1 受體）的文獻與試驗
- 補齊詳細的作用機轉資料（如查詢 DrugBank）
- 取得香港衛生署仿單的警語與禁忌資料，作為安全性篩選依據
- 有初步臨床或前臨床訊號後，再重新評估

安全性資訊請參考原廠仿單。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


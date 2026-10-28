---
layout: default
title: Ribociclib
parent: 中證據等級 (L3-L4)
nav_order: 769
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Ribociclib：預測新適應症為骨髓性白血病 (Myeloid Leukemia)（證據等級 L4）。原適應症：本次資料未載明"
monitor_inn: "RIBOCICLIB"
predicted_indications: ["myeloid leukemia", "thrombocytopenia", "marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets"]
---

# Ribociclib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

## Ribociclib：從（原適應症未載明）到骨髓性白血病
{: .text-alpha }

## 一句話總結

Ribociclib 是一種 CDK4/6 抑制劑，在香港以 KISQALI 品名上市，但本次彙整的資料未載明其核准適應症。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇相關的前臨床文獻**，證據相當有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次資料未載明 |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 0.9935 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold（列為研究問題） |

---

## 為什麼這個預測合理？

Ribociclib 抑制 CDK4/6，這兩種激酶調控細胞週期由 G1 期進入 S 期。急性骨髓性白血病 (AML) 細胞的增殖常依賴 CDK4/6 訊號，因此從機轉上有合理的推論。

一篇 2020 年的前臨床研究（PMID 32560251）指出，CDK4/6 抑制劑可針對 AML 細胞中由 ABCB1、ABCG2 轉運蛋白造成的藥物動力學抗藥性。這提供了合理但間接的依據。

需要注意：該研究是細胞層級的前臨床研究，並非針對 ribociclib 的臨床療效證據。TxGNN 的高分是電腦模型預測，不等於臨床證據。目前也缺乏詳細的作用機轉資料，上述機轉為依 CDK4/6 抑制作用所作的推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | 前臨床／體外研究 | Cancers | CDK4/6 抑制劑可針對 AML 細胞中的藥物動力學抗藥性（ABCB1、ABCG2 轉運蛋白） |

另一篇被檢索到的文獻（PMID 41641105）為外陰乳腺型腺癌的個案報告，與骨髓性白血病無明顯關聯，未列入。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65561 | KISQALI TABLETS 200 MG | 未載明 | 未載明 |

持證商為 Novartis Pharmaceuticals (HK) Limited，狀態為有效的單方製劑。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（CDK4/6 抑制劑） |
| 骨髓抑制風險 | 中至高。文獻顯示嗜中性白血球減少、血小板減少等血液毒性常見 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

本藥在乳癌的研究中已顯示血液毒性，若用於白血病族群，骨髓抑制的疊加風險需要特別評估。

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，其中列為嚴重（Major）的包括：
  - Clarithromycin
  - Dolasetron

  其餘多為中度（Moderate），例如 famotidine、hydrocortisone、metformin、pioglitazone、dexamethasone、aprepitant、loperamide 等。

警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 目前僅有一篇間接的前臨床研究支持，沒有臨床試驗，證據等級為 L4。
- TxGNN 分數雖高，但屬計算預測，且 ribociclib 本身有骨髓抑制的已知風險，用於血液惡性腫瘤需審慎。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料
- 針對 AML 進行更多前臨床驗證（如 ribociclib 本身的細胞株與動物模型）
- 評估血液毒性在白血病患者的可管理性
- 若前臨床結果正向，再規劃早期臨床試驗

---

### 其他預測適應症的說明

排名第 2 至第 4 的預測（血小板低下症及相關遺傳性疾病）**不建議推進**（Hold）：
- **血小板低下症**：文獻顯示血小板低下是 ribociclib 等 CDK4/6 抑制劑的不良反應，並非治療目標，模型預測可能反映的是藥物與疾病的關聯，而非治療關係。
- **巨血小板症合併二尖瓣閉鎖不全**與**遺傳性血小板低下（血小板正常）**：沒有任何文獻或試驗，也無機轉依據，且 ribociclib 已知會造成骨髓抑制。後者的疾病名稱本身自相矛盾，可能是本體標註的問題。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


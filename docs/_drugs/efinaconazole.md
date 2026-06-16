---
layout: default
title: Efinaconazole
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Efinaconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Efinaconazole：從甲真菌病到皮膚肉瘤

## 一句話總結

Efinaconazole 是一種局部外用三唑類抗真菌藥，主要用於甲真菌病（甲癬）的治療。TxGNN 模型以最高排名預測它可能對**皮膚肉瘤 (Skin Sarcoma)** 等 10 種腫瘤疾病有效，然而所有預測均**缺乏臨床試驗與文獻佐證**，加之藥物全身生物利用度極低（~1.6%），整體證據強度停留在 L5。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲真菌病（甲癬，Onychomycosis） |
| 預測新適應症（第一名） | 皮膚肉瘤 (Skin Sarcoma) |
| TxGNN 預測分數 | 50.00% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Efinaconazole 屬三唑類抗真菌藥，其作用機轉為選擇性抑制真菌 **CYP51A1（羊毛固醇 14α-去甲基酶）**，阻斷麥角固醇（ergosterol）的生物合成，進而破壞真菌細胞膜的完整性。臨床上以 10% 局部外用溶液（商品名 Jublia®）核准用於趾甲甲真菌病。目前 Evidence Pack 中作用機轉欄位標記為資料缺口，上述機轉描述來自公開藥理文獻。

就機轉推理而言，部分體外研究顯示膽固醇合成路徑在某些腫瘤細胞的增殖中扮演角色，理論上 CYP51 抑制或許可干擾腫瘤細胞的固醇代謝。然而，本報告所列 10 種腫瘤疾病（皮膚肉瘤、鼻竇未分化癌、印戒細胞胃腺癌、淋巴瘤等）的致病機轉各異，多涉及基因突變、病毒感染或免疫異常，與 CYP51/麥角固醇路徑均**無已知直接關聯**。

最關鍵的藥動學限制在於：Efinaconazole 設計為局部外用製劑，**全身生物利用度僅約 1.6%**，根本無法達到腫瘤治療所需的有效全身血中濃度。這一特性從藥理基礎上削弱了所有全身性腫瘤適應症的可行性，除非對劑型進行根本性改良。

---

## 預測適應症總覽（本次 Top 10）

所有預測分數相同（50.00%），排名均在第 248 萬名以後，顯示模型對此藥物的腫瘤再利用潛力信心極低。

| 排名 | 預測疾病 | TxGNN 分數 | 預測排名 | 機轉關聯性摘要 | 建議 |
|------|---------|-----------|---------|--------------|------|
| 1 | Skin Sarcoma（皮膚肉瘤） | 50% | #2,480,737 | 無直接機轉連結；全身暴露量不足 | Hold |
| 2 | Sinus Histiocytosis with Massive Lymphadenopathy（鼻竇組織細胞增生症） | 50% | #2,480,746 | 免疫失調疾病，與 CYP51 無關聯 | Hold |
| 3 | Sinonasal Undifferentiated Carcinoma（鼻竇未分化癌） | 50% | #2,480,747 | 涉及 TP53/EBV；局部製劑無法覆蓋鼻竇 | Hold |
| 4 | Signet Ring Cell Gastric Adenocarcinoma（印戒細胞胃腺癌） | 50% | #2,480,748 | CDH1/RHOA 突變相關；無機轉連結 | Hold |
| 5 | Sex Hormone-Producing Adrenal Cortex Adenoma（性荷爾蒙分泌性腎上腺皮質腺瘤） | 50% | #2,480,750 | **本組中相對最具機轉合理性**；但生物利用度仍為障礙 | Hold |
| 6 | Small Intestinal Burkitt Lymphoma（小腸 Burkitt 淋巴瘤） | 50% | #2,480,753 | MYC 易位/EBV 相關；與 CYP51 無關聯 | Hold |
| 7 | Small Intestinal DLBCL（小腸瀰漫性大 B 細胞淋巴瘤） | 50% | #2,480,754 | 系統暴露量不足以達治療濃度 | Hold |
| 8 | Small Intestinal EATL（小腸腸病相關 T 細胞淋巴瘤） | 50% | #2,480,755 | JAK-STAT/PI3K 路徑；與 CYP51 無關聯 | Hold |
| 9 | Soft Tissue Neoplasm（軟組織腫瘤） | 50% | #2,480,756 | 異質性類別；無直接實驗數據 | Hold |
| 10 | Submandibular Gland Adenocarcinoma（下頜下腺腺癌） | 50% | #2,480,757 | HER2/NTRK 相關；解剖位置無法覆蓋 | Hold |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（已查詢 ClinicalTrials.gov 及 ICTRP，針對 Efinaconazole 與上述 10 種適應症的所有組合，搜尋結果均為零。）

---

## 文獻證據

目前無相關文獻。

（已查詢 PubMed，針對 Efinaconazole 與上述 10 種適應症的所有組合，搜尋結果均為零。）

---

## 香港上市資訊

Efinaconazole 目前在香港**未上市**，無任何許可證記錄（許可證總數：0）。

如需取得安全性資訊，可參考其他已上市地區的仿單，例如美國 FDA 核准的 Jublia® 仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單（如 Jublia® 美國仿單）。

（本 Evidence Pack 中警語、禁忌症及藥物交互作用資料均缺乏，無法在此列出。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有 10 個預測適應症均為腫瘤疾病，TxGNN 預測分數僅 50%、排名均在第 248 萬名之後，顯示模型信心極低，屬於低優先度預測結果。
- Efinaconazole 極低的全身生物利用度（~1.6%）是針對任何全身性腫瘤適應症的**根本藥動學障礙**，在劑型未根本改良前不具可行性。

**若要推進需要：**
- 補充完整作用機轉資料（DrugBank MOA），以確認 CYP51 抑制對人類細胞固醇代謝的潛在效應
- 取得香港衛生署或 TFDA 仿單以評估完整安全性輪廓
- 若評估三唑類在腎上腺皮質腺瘤（Rank 5，機轉合理性最高）的潛力，應優先回顧系統性三唑類藥物（如 Ketoconazole）的既有數據作為類比參照
- 考慮是否有提高全身生物利用度的劑型改良可能性（如口服劑型研發），方能解鎖全身性腫瘤適應症的再利用路徑

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。所有老藥新用候選需經嚴謹的臨床驗證方可應用於患者照護。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


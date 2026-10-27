---
layout: default
title: Framycetin
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Framycetin：預測新適應症為硬化性膽管炎 (Sclerosing Cholangitis)（證據等級 L5）。原適應症：香港許可證未載明適應症文字"
monitor_inn: "Framycetin"
predicted_indications: ["sclerosing cholangitis", "urinary tract infection (disease)", "congenital prothrombin deficiency", "gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
---

# Framycetin
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

## Framycetin：從（原適應症未載明）到硬化性膽管炎
{: .text-alpha }

## 一句話總結

Framycetin 是一種胺基糖苷類抗生素，口服吸收差，主要作用於腸道內或局部使用。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬於模型的計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字 |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Framycetin 屬於胺基糖苷類抗生素，這類藥物對革蘭氏陰性菌有廣泛活性，且 framycetin 口服吸收差，主要作用於腸道內。

理論上，腸道限制性抗生素可能影響腸－肝軸與微生物相關的膽道發炎，這也是口服 vancomycin 被研究用於原發性硬化性膽管炎的理由。不過，胺基糖苷類並非此疾病的既定治療類別，也沒有針對 framycetin 的試驗或文獻。

因此，0.997 的高分僅是計算預測，不能視為臨床有效的證據。

**其他預測適應症（皆為 L5、Hold，僅供參考）：**

| 排名 | 預測適應症 | TxGNN 分數 | 簡評 |
|------|-----------|-----------|------|
| 2 | 泌尿道感染 | 99.42% | 對革蘭氏陰性菌有活性，生物學上合理；但全身吸收差且有腎毒性、耳毒性疑慮，不適合全身治療 |
| 3 | 先天性凝血酶原缺乏症 | 99.41% | 未發現合理機轉，可能是圖譜運算的假象 |
| 4 | 淋球菌性尿道炎 | 99.28% | 同類藥物曾用於淋病，但現行指引因抗藥性改用其他藥物 |
| 5 | Ureaplasma 尿道炎 | 99.28% | 抗菌理由薄弱，一線為四環素與巨環內酯類 |
| 6 | 子宮發炎性疾病 | 99.18% | 同類藥物（如 gentamicin）用於骨盆腔發炎，但 framycetin 全身吸收差 |
| 7 | 黃色肉芽腫性腎盂腎炎 | 99.18% | 通常需手術合併抗生素，framycetin 不太可能適用 |

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
| HK-67429 | CANAURAL EAR DROPS, SUSPENSION FOR DOGS AND CATS (VET) | 未載明 | 未載明 |

此許可證為動物用（犬貓）耳用滴劑，製造商為 ALFAMEDIC LIMITED，並非人用藥品。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都僅有模型預測，沒有臨床試驗或文獻（L5）。
- 香港唯一的許可證是動物用耳用滴劑，與預測的人類適應症之間缺乏直接關聯，且 framycetin 全身吸收差，並有腎毒性與耳毒性疑慮。

**若要推進需要：**
- 補充作用機轉資料（MOA），釐清腸道限制性抗生素與膽道發炎的關聯。
- 取得安全性資料（仿單警語與禁忌）。
- 進行文獻與臨床試驗的系統性檢索，確認硬化性膽管炎是否有胺基糖苷類的研究。
- 評估給藥途徑是否與預測適應症相容（目前許可證僅有耳用劑型）。
- 若仍想探索，可先進行前臨床研究，或與已有證據的 vancomycin 等腸道限制性抗生素比較。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


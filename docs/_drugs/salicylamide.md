---
layout: default
title: Salicylamide
parent: 僅模型預測 (L5)
nav_order: 798
evidence_level: L5
indication_count: 9
monitor_inn: "SALICYLAMIDE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria", "lung disease", "massive neonatal aspiration syndrome", "respiratory syncytial virus bronchiolitis", "hantavirus infectious disease"]
last_modified_at: 2026-11-24
description: "Salicylamide：預測新適應症為咽炎 (Pharyngitis)（證據等級 L5）。原適應症：頭痛"
---

# Salicylamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Salicylamide：從頭痛到咽炎
{: .text-alpha }

## 一句話總結

Salicylamide（水楊酸胺）是一種具止痛與退燒作用的藥物，知識圖譜中記錄的原適應症為頭痛 (headache disorder)。
TxGNN 模型預測它可能對**咽炎 (Pharyngitis)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇** 1953 年的舊病例報告，證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 頭痛（知識圖譜中記錄的關聯；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 咽炎 (Pharyngitis) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5（唯一一篇文獻為 1953 年、針對嬰兒卡他性扁桃腺炎的報告，未直接研究咽炎本身） |
| 香港上市 | 上市中（有效許可證 101 張／共 101 張） |
| 許可證數 | 101 張（有效 101 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Salicylamide 具有止痛與退燒作用，機轉上可能緩解咽喉疼痛與發燒等症狀。

這個關聯屬於「症狀緩解」層次，而非針對咽炎病因的治療。唯一的文獻是 1953 年一份嬰兒卡他性扁桃腺炎的報告，使用 salicylamide 搭配對胺基苯甲酸鈉，屬於舊式、低品質的臨床報告，且為複合使用，無法單獨判斷 salicylamide 的貢獻。TxGNN 的高分僅是模型預測，不能視為療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [13060598](https://pubmed.ncbi.nlm.nih.gov/13060598/) | 1953 | 病例系列／臨床報告 | Gazzetta medica italiana | 以 salicylamide 搭配對胺基苯甲酸鈉治療嬰兒卡他性扁桃腺炎；無摘要，非對照研究 |

## 香港上市資訊

以下為資料中列出的部分許可證（共 101 張含本藥成分的許可證，全部有效，皆為複方）。資料中未載明劑型與核准適應症文字。

<!-- review:begin hk-lic-20261117-salicylamide-1 -->

> **查核更正（2026-11-17）**：原文為「以下為資料中列出的部分許可證（至少 20 張，清單可能不完整），均為單一成分製劑、狀態有效。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 101 張含本藥成分的許可證（全部有效；皆為複方）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-salicylamide-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-07880 | COLDZEP TAB | 複方 | MEYER PHARMACEUTICALS LTD | 有效 |
| HK-26015 | NEO-COLD CAP | 複方 | UNICORN LABORATORIES O/B AMERICAN UNICORN LABORATORIES LIMITED | 有效 |
| HK-31316 | COLIDIN TAB | 複方 | MEYER PHARMACEUTICALS LTD | 有效 |
| HK-07883 | MECOLD (FORTE) CAP | 複方 | MEYER PHARMACEUTICALS LTD | 有效 |
| HK-07882 | MECOLD (SCT) RED TAB | 複方 | MEYER PHARMACEUTICALS LTD | 有效 |

上表列出其中 5 張（共 101 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：高血壓、肝衰竭、肝病、腎病、癲癇、慢性阻塞性肺病、消化性潰瘍、胃炎、發炎性腸病、血小板低下、凝血疾病、血友病、貧血、糖尿病、痛風、甲狀腺功能低下、藥物濫用／依賴等。
- **過敏相關**：文獻指出，阿斯匹靈敏感或止痛劑誘發氣喘的患者，需留意解熱鎮痛藥的交叉反應；另有 1979 年小型研究顯示 salicylamide 在 18 名此類患者中耐受良好，但證據有限。
- 具體警語、禁忌與藥物交互作用，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症沒有任何臨床試驗，僅有一篇 1953 年的低品質報告，證據等級為 L5。
- 預測屬症狀緩解性質，且仿單安全性資料尚缺，不宜推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌
- 補充作用機轉資料
- 設計針對咽炎的對照臨床研究，與現有解熱鎮痛藥比較
- 評估知識圖譜所列禁忌族群的安全性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「以下為資料中列出的部分許可證（至少 20 張，清單可能不完整），均為單一成分製劑」→「以下為資料中列出的部分許可證（共 101 張含本藥成分的許可」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---


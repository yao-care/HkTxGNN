---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 820
evidence_level: L5
indication_count: 8
monitor_inn: "SODIUM CITRATE"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "stomach disease", "postgastrectomy syndrome", "gastroduodenitis", "familial visceral myopathy", "rosacea conjunctivitis", "allergic urticaria"]
last_modified_at: 2026-10-28
description: "Sodium Citrate：預測新適應症為乳頭狀結膜炎（證據等級 L5）。原適應症：知識圖譜記錄的關聯：消化性潰瘍、胃食道逆流、食道炎、消化不良、咽炎、感冒、鼻炎、鼻咽炎"
---

# Sodium Citrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## 檸檬酸鈉（Sodium Citrate）：從消化性潰瘍與胃食道逆流到乳頭狀結膜炎
{: .text-alpha }

## 一句話總結

檸檬酸鈉是一種緩衝劑與制酸成分，在知識圖譜中記錄的使用範圍包括消化性潰瘍、胃食道逆流、消化不良及上呼吸道不適等。
TxGNN 模型預測它可能對**乳頭狀結膜炎 (Papillary Conjunctivitis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：消化性潰瘍、胃食道逆流、食道炎、消化不良、咽炎、感冒、鼻炎、鼻咽炎（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 乳頭狀結膜炎 |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，檸檬酸鈉是一種緩衝劑，可中和酸性環境，也具有鈣離子螯合作用。在消化道相關用途上，其制酸緩衝特性與消化性潰瘍、胃食道逆流、消化不良等知識圖譜記錄的關聯相符。

至於乳突狀結膜炎，目前沒有資料支持檸檬酸鈉對此疾病有效。可能的推測是：檸檬酸緩衝或鈣螯合作用也許能調節眼表局部 pH 或發炎反應，但這只是未經驗證的假設。高分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不代表生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（補充：預測排名第 3 的「胃部疾病」有若干文獻，但多為胃癌細胞與動物的前臨床研究，或與檸檬酸鈉療效無直接關係的研究；這些並未直接研究乳頭狀結膜炎，故不列入本預測的證據。）

---

## 香港上市資訊

資料顯示至少有 20 張有效的單一成分許可證（清單可能不完整），以下列出 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-28241 | SOD CITRATE SOLN 3.13% (B BRAUN) | 未載明 | 未載明 |
| HK-65289 | REGIOCIT SOLUTION FOR HAEMOFILTRATION | 未載明 | 未載明 |
| HK-49787 | BENA EXPECTORANT | 未載明 | 未載明 |
| HK-47398 | DIPHENHYDRAMINE COMP LINCTUS | 未載明 | 未載明 |
| HK-46401 | DIPHENHYDRAMINE COMP. LINCTUS | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：高血壓、胰臟炎、腎上腺皮質功能不全、艾迪森氏症、良性攝護腺增生、無尿、橫紋肌溶解、高血鈣、腎鈣化、冠狀動脈疾病、心肌梗塞、腎功能不全、代謝性酸中毒、隅角閉鎖型青光眼、先天性腎上腺增生等。
- **藥物交互作用**（共 100 筆，以下為主要項目）：
  - 重大：氫氧化鋁（Aluminum hydroxide）
  - 中度：Doxycycline、Tetracycline、Minocycline、Levofloxacin、阿斯匹靈、鐵劑、麻黃素、偽麻黃素、Rosuvastatin、Acalabrutinib
  - 輕微：Sulfonylurea 類降血糖藥（Glipizide、Glyburide 等）、Lactulose、Misoprostol

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 針對乳突狀結膜炎沒有任何臨床試驗或文獻，預測僅來自 TxGNN 模型（深度學習），證據等級為 L5。
- 作用機轉資料缺乏，且仿單層級的安全性資訊尚未取得。

**若要推進需要：**
- 補齊作用機轉資料與香港仿單的警語、禁忌資訊
- 進行眼表局部使用的文獻回顧與前臨床研究（例如眼表 pH、發炎模型），確認機轉可行性
- 評估眼用劑型與給藥途徑的可行性及眼部耐受性
- 若前臨床結果正面，再規劃小規模探索性臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

